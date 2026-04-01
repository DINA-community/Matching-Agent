"""
Database models for the DINA cache database.

This module defines the SQLAlchemy ORM models representing the cache database schema.
It includes models for user authentication, asset and CSAF product management,
matching operations, and synchronization metadata. All models inherit from a common
Base class and reside in the 'cacheDB' schema.

The module provides hierarchical product relationships through both assets and CSAF
products, along with tracking mechanisms for synchronization runs and matching operations.
"""

import datetime
import enum
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional

from pwdlib import PasswordHash
from sqlalchemy import (
    CheckConstraint,
    Column,
    Dialect,
    Enum,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    Table,
    Text,
    TypeDecorator,
    Index,
)
from sqlalchemy.dialects.postgresql import JSONB

# from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from dina.common.log import get_logger

logger = get_logger(__name__)

password_hash = PasswordHash.recommended()


class MetaInfo:
    """
    Mixin class providing metadata fields for tracking resource origin and updates.

    This class is intended to be inherited by ORM models that need to track
    resource provenance and modification timestamps. It provides standardized
    fields for origin tracking and update history.

    :ivar origin_uri: URI base of the originating resource.
    :type origin_uri: str
    :ivar origin_info: Additional JSON-formatted information
        about the origin of the resource, if provided.
    :type origin_info: Optional[dict]
    :ivar uri: The URI of the resource.
    :type uri: str
    :ivar last_update: The timestamp (Unix epoch) of the last
        update for the resource.
    :type last_update: float
    """

    origin_uri: Mapped[str] = mapped_column(Text)
    origin_info: Mapped[dict[str, Any]] = mapped_column(JSONB, default={})
    uri: Mapped[str] = mapped_column(Text)
    last_update: Mapped[float] = mapped_column(Float)


class Base(AsyncAttrs, DeclarativeBase):
    """
    Base class for all ORM models in the cache database.

    All database models inherit from this base, which configures async support
    and sets the database schema to 'cacheDB'.
    """

    metadata = MetaData(schema="cacheDB")


class User(Base):
    """
    Represents an authenticated user in the system.

    This model stores user credentials and account status. Passwords are hashed
    using the pwdlib library before storage.

    :ivar username: Unique username serving as the primary key.
    :ivar password_hash: Hashed password for authentication.
    :ivar active: Whether the user account is active.
    """

    __tablename__ = "users"
    username: Mapped[str] = mapped_column(Text, primary_key=True)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    active: Mapped[bool] = mapped_column(nullable=False, default=True)

    def set_password(self, password: str):
        """
        Hash and store the provided password.

        :param password: Plain text password to hash and store.
        """
        self.password_hash = password_hash.hash(password)

    def check_password(self, password: str) -> bool:
        """
        Verify a password against the stored hash.

        :param password: Plain text password to verify.
        :return: True if the password matches, False otherwise.
        """
        return password_hash.verify(password, self.password_hash)


class SynchronizerMetadata(Base):
    """
    Tracks metadata and execution state for data source synchronizers.

    Each record represents the synchronization state for a specific origin URI,
    storing plugin-specific metadata and the timestamp of the last successful run.

    :ivar origin_uri: URI identifying the data source (primary key).
    :ivar plugin_metadata: Plugin-specific metadata stored as JSON.
    :ivar last_run: Timestamp of the most recent synchronization run.
    """

    __tablename__ = "synchronizer_metadata"
    origin_uri: Mapped[str] = mapped_column(Text, primary_key=True)
    plugin_metadata: Mapped[dict[str, Any]] = mapped_column(JSONB, default={})
    last_run: Mapped[datetime.datetime] = mapped_column(
        nullable=False, default=datetime.datetime.fromtimestamp(0.0)
    )


class MatcherTrigger(Base):
    """
    Records requests to trigger the matcher process.

    Used to queue and track matcher execution requests, optionally scoped
    to a specific origin URI.

    :ivar id: Auto-incrementing primary key.
    :ivar origin_uri: Optional URI to limit matching scope.
    :ivar created_at: Timestamp when the trigger was created.
    """

    __tablename__ = "matcher_trigger"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    origin_uri: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[float] = mapped_column(
        Float, default=lambda: datetime.datetime.now().timestamp()
    )


class MatcherRun(Base):
    """
    Represents a single execution of the matcher process.

    Tracks the complete lifecycle of a matching run, including progress metrics,
    configuration, and resulting matches. The state field indicates whether the
    run is ongoing, completed, or failed.

    :ivar id: Auto-incrementing primary key.
    :ivar trigger: Description of what triggered this run.
    :ivar state: Current state of the run (e.g., 'running', 'completed', 'failed').
    :ivar started_at: Timestamp when the run began.
    :ivar finished_at: Timestamp when the run completed (None if still running).
    :ivar total_pairs: Total number of asset-CSAF pairs to evaluate.
    :ivar processed_pairs: Number of pairs processed so far.
    :ivar matches_found: Number of matches identified.
    :ivar assets: List of asset URIs included in this run.
    :ivar csaf_documents: List of CSAF document URIs included in this run.
    :ivar matching_config_hash: Hash of the matching configuration used.
    :ivar matching_config: The actual matching configuration as JSON.
    :ivar force_recompute: Whether this run forced recomputation of all matches.
    :ivar error: Error message if the run failed.
    :ivar matches: Relationship to Match records created by this run.
    """

    __tablename__ = "matcher_run"
    __table_args__ = (Index("ix_matcher_run_started_at", "started_at"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    trigger: Mapped[str] = mapped_column(Text, nullable=False)
    state: Mapped[str] = mapped_column(Text, nullable=False, default="running")
    started_at: Mapped[float] = mapped_column(
        Float, nullable=False, default=lambda: datetime.datetime.now().timestamp()
    )
    finished_at: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    total_pairs: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    processed_pairs: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    matches_found: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    assets: Mapped[List[str]] = mapped_column(JSONB, nullable=False, default=list)
    csaf_documents: Mapped[List[str]] = mapped_column(
        JSONB, nullable=False, default=list
    )
    matching_config_hash: Mapped[str] = mapped_column(Text, nullable=False)
    matching_config: Mapped[dict[str, Any]] = mapped_column(
        JSONB, nullable=False, default=dict
    )
    force_recompute: Mapped[bool] = mapped_column(nullable=False, default=False)
    error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    matches: Mapped[List["Match"]] = relationship(back_populates="matcher_run")

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the matcher run to a dictionary representation.

        :return: Dictionary containing all matcher run fields.
        """
        result: Dict[str, Any] = {
            "trigger": self.trigger,
            "state": self.state,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "total_pairs": self.total_pairs,
            "processed_pairs": self.processed_pairs,
            "matches_found": self.matches_found,
            "assets": self.assets,
            "csaf_documents": self.csaf_documents,
            "matching_config_hash": self.matching_config_hash,
            "matching_config": self.matching_config,
            "force_recompute": self.force_recompute,
            "error": self.error,
        }
        if self.id is not None:
            result["id"] = self.id
        return result


class ProductType(enum.Enum):
    """
    Enumeration of product types.

    Distinguishes between software products, hardware devices, hardware modules,
    and undefined types.
    """

    Software = "Software"
    Device = "Device"
    Module = "Module"
    Undefined = "Undefined"


@dataclass
class File:
    """
    Represents a file with its cryptographic hash.

    :ivar name: The filename.
    :ivar file_hash: The hash value of the file.
    :ivar hash_algorithm: The algorithm used to compute the hash.
    """

    name: str
    file_hash: str
    hash_algorithm: str


@dataclass
class FileList:
    """
    Container for a list of File objects.

    Provides a structured way to store multiple files as a collection.
    """

    files: List[File] = field(default_factory=list)


class FileListType(TypeDecorator):
    """
    SQLAlchemy custom type for storing FileList objects as JSONB.

    Handles bidirectional conversion between FileList instances and their
    JSON representation for database storage.
    """

    impl = JSONB
    cache_ok = True

    def process_bind_param(
        self, value: Optional[FileList], dialect: Dialect
    ) -> Optional[List[Dict[str, str]]]:
        """
        Convert FileList to JSON for database storage.

        :param value: FileList instance to convert.
        :param dialect: SQLAlchemy dialect (unused).
        :return: List of file dictionaries or empty list if None.
        :raises TypeError: If value is not a FileList instance.
        """
        if value is None:
            return []
        if isinstance(value, FileList):
            return [asdict(item) for item in value.files]
        raise TypeError(f"Expected FileList, got {type(value)}")

    def process_result_value(
        self, value: Optional[Any], dialect: Dialect
    ) -> Optional[FileList]:
        """
        Convert JSON from database to FileList instance.

        :param value: JSON data from database.
        :param dialect: SQLAlchemy dialect (unused).
        :return: FileList instance or empty FileList if None.
        :raises TypeError: If value is not a list.
        """
        if value is None:
            return FileList(files=[])
        if isinstance(value, list):
            return FileList(files=[File(**file) for file in value])
        raise TypeError(f"Expected list, got {type(value)}")


class Product(Base):
    """
    Represents product information extracted from either assets or CSAF documents.

    A Product record consolidates identifying information about a software or hardware
    product. Each Product is associated with exactly one Asset OR one CsafProduct
    (enforced by database constraint).

    Supports both software identifiers (CPE, PURL, version) and device-specific
    attributes (model, part numbers, manufacturer).

    :ivar id: Auto-incrementing primary key.
    :ivar product_type: Type of product (Software, Device, Module, or Undefined).
    :ivar name: Product name.
    :ivar version: List of version strings.
    :ivar cpe: Common Platform Enumeration identifier.
    :ivar purl: Package URL identifier.
    :ivar sbom_urls: List of Software Bill of Materials URLs.
    :ivar serial_numbers: List of device serial numbers.
    :ivar files: List of associated files with hashes.
    :ivar model: Device model identifier.
    :ivar model_numbers: List of model numbers.
    :ivar part_numbers: List of part numbers.
    :ivar device_family: Device family/series name.
    :ivar hardware_name: Hardware platform name.
    :ivar manufacturer_name: Manufacturer/vendor name.
    :ivar csaf_product_id: Foreign key to CsafProduct (mutually exclusive with asset_id).
    :ivar asset_id: Foreign key to Asset (mutually exclusive with csaf_product_id).
    :ivar csaf_product: Relationship to the associated CsafProduct.
    :ivar asset: Relationship to the associated Asset.
    """

    __tablename__ = "product"
    __table_args__ = (
        CheckConstraint(
            "(csaf_product_id IS NULL) != (asset_id IS NULL)",
            name="check_exclusive_foreign_keys",
        ),
        Index("product_ix_csaf_product_id", "csaf_product_id", unique=True),
        Index("product_ix_asset_id", "asset_id", unique=True),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_type: Mapped[ProductType] = mapped_column(
        Enum(
            ProductType,
            name="product_type_enum",
            schema="cacheDB",
            inherit_schema=True,
        ),
        default=ProductType.Undefined,
    )
    name: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    version: Mapped[List[str]] = mapped_column(JSONB, nullable=True)
    cpe: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    purl: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    sbom_urls: Mapped[List[str]] = mapped_column(JSONB, default=[])
    serial_numbers: Mapped[List[str]] = mapped_column(JSONB, default=[])
    files: Mapped[FileList] = mapped_column(FileListType, default=FileList(files=[]))

    # Device Type information
    model: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    model_numbers: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    part_numbers: Mapped[Optional[List[str]]] = mapped_column(JSONB, nullable=True)
    device_family: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    hardware_name: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    manufacturer_name: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    csaf_product_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("cacheDB.csaf_product.id", ondelete="CASCADE"),
        nullable=True,
    )
    asset_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("cacheDB.asset.id", ondelete="CASCADE"), nullable=True
    )

    csaf_product: Mapped[Optional["CsafProduct"]] = relationship(
        back_populates="product", passive_deletes=True
    )
    asset: Mapped[Optional["Asset"]] = relationship(
        back_populates="product", passive_deletes=True
    )

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the product to a dictionary representation.

        :return: Dictionary containing all product fields.
        """
        result = {
            "product_type": self.product_type.value,
            "name": self.name,
            "version": self.version,
            "cpe": self.cpe,
            "purl": self.purl,
            "sbom_urls": self.sbom_urls,
            "serial_numbers": self.serial_numbers,
            "files": self.files,
            "model": self.model,
            "model_numbers": self.model_numbers,
            "part_numbers": self.part_numbers,
            "device_family": self.device_family,
            "hardware_name": self.hardware_name,
            "manufacturer_name": self.manufacturer_name,
            "csaf_product_id": self.csaf_product_id,
            "asset_id": self.asset_id,
        }
        if self.id is not None:
            result["id"] = self.id
        return result


csaf_product_relationship = Table(
    "csaf_product_relationship",
    Base.metadata,
    Column(
        "parent_id",
        Integer,
        ForeignKey("cacheDB.csaf_product.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "child_id",
        Integer,
        ForeignKey("cacheDB.csaf_product.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("origin_uri", Text, nullable=False),
    Column("origin_info", JSONB, default={}),
    Column("last_update", Float, nullable=False, default=0.0),
)
"""
Association table for hierarchical relationships between CSAF products.

Enables parent-child relationships between CsafProduct instances, storing
metadata about the relationship origin and last update timestamp.
"""


class CsafProduct(Base, MetaInfo):
    """
    Represents a product referenced in a CSAF security advisory document.

    Each CsafProduct has exactly one associated Product record containing the
    product details, and can participate in parent-child relationships with
    other CSAF products. CSAF products can be matched against Assets.

    :ivar id: Auto-incrementing primary key.
    :ivar product: One-to-one relationship with the Product record.
    :ivar matches: All matches between this CSAF product and assets.
    :ivar children: Child CSAF products in the product hierarchy.
    :ivar parents: Parent CSAF products in the product hierarchy.
    """

    __tablename__ = "csaf_product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # A CsafProduct has exactly one Product entry
    product: Mapped["Product"] = relationship(
        back_populates="csaf_product", passive_deletes=True
    )

    # A CsafProduct can be associated with multiple matches
    matches: Mapped[List["Match"]] = relationship(
        back_populates="csaf_product", passive_deletes=True
    )

    children: Mapped[List["CsafProduct"]] = relationship(
        "CsafProduct",
        secondary=csaf_product_relationship,
        primaryjoin=id == csaf_product_relationship.c.parent_id,
        secondaryjoin=id == csaf_product_relationship.c.child_id,
        back_populates="parents",
    )
    parents: Mapped[List["CsafProduct"]] = relationship(
        "CsafProduct",
        secondary=csaf_product_relationship,
        primaryjoin=id == csaf_product_relationship.c.child_id,
        secondaryjoin=id == csaf_product_relationship.c.parent_id,
        back_populates="children",
    )

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the CSAF product to a dictionary representation.

        :return: Dictionary containing metadata fields and ID.
        """
        result = {
            "origin_uri": self.origin_uri,
            "origin_info": self.origin_info,
            "last_update": self.last_update,
            "uri": self.uri,
        }
        if self.id is not None:
            result["id"] = self.id
        return result

    def document_url(self) -> str:
        """
        Generate the URL for the CSAF document associated with this product.

        :return: URL string for the CSAF document.
        """
        return str(self.origin_uri) + f"{self.origin_info['path']}".lstrip("/")

    def product_id(self) -> str:
        """
        Retrieve the product ID associated with this CSAF document.

        :return: Product ID as an integer.
        """
        return self.origin_info["product_name_id"]


product_relationship = Table(
    "product_relationship",
    Base.metadata,
    Column(
        "parent_id",
        Integer,
        ForeignKey("cacheDB.asset.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "child_id",
        Integer,
        ForeignKey("cacheDB.asset.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("origin_uri", Text, nullable=False),
    Column("origin_info", JSONB, default={}),
    Column("last_update", Float, nullable=False, default=0.0),
)
"""
Association table for hierarchical relationships between assets.

Enables parent-child relationships between Asset instances, storing
metadata about the relationship origin and last update timestamp.
"""


class Asset(Base, MetaInfo):
    """
    Represents a product instance from an asset inventory system.

    Each Asset has exactly one associated Product record containing the
    product details, and can participate in parent-child relationships with
    other assets. Assets can be matched against CSAF products.

    :ivar id: Auto-incrementing primary key.
    :ivar product: One-to-one relationship with the Product record.
    :ivar matches: All matches between this asset and CSAF products.
    :ivar children: Child assets in the asset hierarchy.
    :ivar parents: Parent assets in the asset hierarchy.
    """

    __tablename__ = "asset"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # An Asset has exactly one Product entry
    product: Mapped["Product"] = relationship(
        back_populates="asset", passive_deletes=True
    )

    # An Asset can be associated with multiple matches
    matches: Mapped[List["Match"]] = relationship(
        back_populates="asset", passive_deletes=True
    )

    children: Mapped[List["Asset"]] = relationship(
        "Asset",
        secondary=product_relationship,
        primaryjoin=id == product_relationship.c.parent_id,
        secondaryjoin=id == product_relationship.c.child_id,
        back_populates="parents",
    )
    parents: Mapped[List["Asset"]] = relationship(
        "Asset",
        secondary=product_relationship,
        primaryjoin=id == product_relationship.c.child_id,
        secondaryjoin=id == product_relationship.c.parent_id,
        back_populates="children",
    )

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the asset to a dictionary representation.

        :return: Dictionary containing metadata fields and ID.
        """
        result = {
            "origin_uri": self.origin_uri,
            "origin_info": self.origin_info,
            "uri": self.uri,
            "last_update": self.last_update,
        }
        if self.id is not None:
            result["id"] = self.id
        return result


class Match(Base):
    """
    Represents a match between a CSAF product and an asset.

    Matches are created by the matcher process and indicate potential applicability
    of security advisories to specific assets. Each match includes a confidence score
    and tracks the configuration used to generate it.

    :ivar id: Auto-incrementing primary key.
    :ivar score: Confidence score of the match (0.0 to 1.0).
    :ivar status: Current status of the match (e.g., 'confirmed', 'rejected').
    :ivar timestamp: When the match was created.
    :ivar csaf_product_id: Foreign key to the CSAF product.
    :ivar asset_id: Foreign key to the asset.
    :ivar matcher_run_id: Foreign key to the run that created this match (nullable).
    :ivar trace_uuid: Stable UUID assigned before scoring for traceability.
    :ivar matching_config_hash: Hash of the matching configuration used.
    :ivar csaf_product: Relationship to the CsafProduct.
    :ivar asset: Relationship to the Asset.
    :ivar matcher_run: Relationship to the MatcherRun that created this match.
    """

    __tablename__ = "match"
    __table_args__ = (
        Index("ix_match_csaf_product_id", "csaf_product_id"),
        Index("ix_match_asset_id", "asset_id"),
        Index("ix_match_matcher_run_id", "matcher_run_id"),
        Index("ix_match_trace_uuid", "trace_uuid"),
        Index("ix_match_csaf_product_asset", "csaf_product_id", "asset_id"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    score: Mapped[float] = mapped_column(nullable=False)
    # TODO: Introduce enum for match status?
    status: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[float] = mapped_column(nullable=False)
    csaf_product_id: Mapped[int] = mapped_column(
        ForeignKey("cacheDB.csaf_product.id", ondelete="CASCADE"), nullable=False
    )
    asset_id: Mapped[int] = mapped_column(
        ForeignKey("cacheDB.asset.id", ondelete="CASCADE"), nullable=False
    )
    matcher_run_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("cacheDB.matcher_run.id", ondelete="SET NULL"), nullable=True
    )
    trace_uuid: Mapped[str] = mapped_column(Text, nullable=False)
    matching_config_hash: Mapped[str] = mapped_column(Text, nullable=False)

    csaf_product: Mapped["CsafProduct"] = relationship(back_populates="matches")
    asset: Mapped["Asset"] = relationship(back_populates="matches")
    matcher_run: Mapped[Optional["MatcherRun"]] = relationship(back_populates="matches")

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the match to a dictionary representation.

        :return: Dictionary containing all match fields.
        """
        result = {
            "score": self.score,
            "status": self.status,
            "timestamp": self.timestamp,
            "csaf_product_id": self.csaf_product_id,
            "asset_id": self.asset_id,
            "matcher_run_id": self.matcher_run_id,
            "trace_uuid": self.trace_uuid,
            "matching_config_hash": self.matching_config_hash,
        }
        if self.id is not None:
            result["id"] = self.id
        return result
