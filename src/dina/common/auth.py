"""
Authentication and authorization module for the DINA application.

This module provides JWT-based authentication functionality for FastAPI applications,
including token creation, validation, and session management. It requires a JWT_SECRET_KEY
environment variable to be set for secure token signing.

The module integrates with FastAPI's OAuth2 password bearer scheme and validates
user sessions against the CacheDB to ensure active user status.
"""

import os
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from dotenv import load_dotenv, find_dotenv
from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from pydantic import BaseModel, ValidationError

from dina.cachedb.database import CacheDB

load_dotenv(find_dotenv(usecwd=True))

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if SECRET_KEY is None:
    exit(
        "JWT_SECRET_KEY not set. Please set the envrionment variable to a securely generated random value.\n"
        'Use for example `echo "export JWT_SECRET_KEY=$(openssl rand -hex 32)" >> .env` to generate a random key.\n'
        "The key is added to a local .env file which is loaded by the executable."
    )
ALGORITHM = "HS256"


class Token(BaseModel):
    """
    OAuth2 token response model.

    Attributes:
        access_token: The JWT access token string
        token_type: The type of token, typically "bearer"
    """

    access_token: str
    token_type: str


class SessionData(BaseModel):
    """
    User session information extracted from JWT tokens.

    Attributes:
        username: The authenticated user's username
    """

    username: str


def create_access_token(data: SessionData, expires_delta: timedelta):
    """
    Create a new JWT access token for a user session.

    Args:
        data: Session data to encode in the token
        expires_delta: Time duration until the token expires

    Returns:
        str: Encoded JWT token string

    Note:
        The token is signed using the JWT_SECRET_KEY from environment variables
        and includes an expiration timestamp.
    """
    to_encode = data.model_dump()
    to_encode.update({"exp": datetime.now(timezone.utc) + expires_delta})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AccessChecker:
    """
    FastAPI dependency for validating JWT tokens and checking user access.

    This class can be used as a FastAPI dependency to protect endpoints by
    validating the JWT token and ensuring the user is active in the database.

    Args:
        db: CacheDB instance for user status validation

    Raises:
        HTTPException: Returns 401 UNAUTHORIZED if token is invalid, expired,
                      or user is not active

    Usage:
        access_checker = AccessChecker(db)

        @app.get("/protected")
        async def protected_route(session: SessionData = Depends(access_checker)):
            return {"user": session.username}
    """

    def __init__(self, db: CacheDB) -> None:
        self.__db = db

    async def __call__(
        self, token: Annotated[str, Depends(oauth2_scheme)]
    ) -> SessionData:
        """
        Validate the provided JWT token and return session data.

        Args:
            token: JWT token string extracted by OAuth2PasswordBearer

        Returns:
            SessionData: Validated session information

        Raises:
            HTTPException: 401 UNAUTHORIZED if validation fails
        """
        cred_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            session = SessionData.model_validate(payload)
            if not await self.__db.user_active(session.username):
                raise cred_exception
            return session
        except (InvalidTokenError, ValidationError):
            raise cred_exception
