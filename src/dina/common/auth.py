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
    access_token: str
    token_type: str


class SessionData(BaseModel):
    username: str


def create_access_token(data: SessionData, expires_delta: timedelta):
    to_encode = data.model_dump()
    to_encode.update({"exp": datetime.now(timezone.utc) + expires_delta})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AccessChecker:
    def __init__(self, db: CacheDB) -> None:
        self.__db = db

    async def __call__(
        self, token: Annotated[str, Depends(oauth2_scheme)]
    ) -> SessionData:
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
