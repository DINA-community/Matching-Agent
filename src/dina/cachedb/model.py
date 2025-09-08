import datetime
import enum
import logging
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional

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
)
from sqlalchemy.dialects.postgresql import JSONB

# from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

logger = logging.getLogger(__name__)


class MetaInfo:
    """
    Represents metadata information related to a resource.

    The MetaInfo class is a representation for defining metadata
    about a specific resource, such as origin details and the
    timestamp of the latest update. It provides a structured
    way to encapsulate this information for consistent access
    and manipulation.

    :ivar origin_uri: URI base of the originating resource.
    :type origin_uri: str
    :ivar origin_info: Additional JSON-formatted information
        about the origin of the resource, if provided.
    :type origin_info: Optional[dict]
    :ivar last_update: The timestamp (Unix epoch) of the last
        update for the resource.
    :type last_update: float
    """

    origin_uri: Mapped[str] = mapped_column(Text)
    origin_info: Mapped[dict[str, Any]] = mapped_column(JSONB, default={})
    last_update: Mapped[float] = mapped_column(Float)


class Base(AsyncAttrs, DeclarativeBase):
    metadata = MetaData(schema="cacheDB")


class SynchronizerMetadata(Base):
    __tablename__ = "synchronizer_metadata"
    origin_uri: Mapped[str] = mapped_column(Text, primary_key=True)
    plugin_metadata: Mapped[dict[str, Any]] = mapped_column(JSONB, default={})
    last_run: Mapped[datetime.datetime] = mapped_column(
        nullable=False, default=datetime.datetime.fromtimestamp(0.0)
    )


class ProductType(enum.Enum):
    Software = "Software"
    Device = "Device"
    Undefined = "Undefined"


@dataclass
class File:
    name: str
    file_hash: str
    hash_algorithm: str


@dataclass
class FileList:
    files: List[File] = field(default_factory=list)


class FileListType(TypeDecorator):
    impl = JSONB
    cache_ok = True

    def process_bind_param(
        self, value: Optional[FileList], dialect: Dialect
    ) -> Optional[List[Dict[str, str]]]:
        if value is None:
            return []
        if isinstance(value, FileList):
            return [asdict(item) for item in value.files]
        raise TypeError(f"Expected FileList, got {type(value)}")

    def process_result_value(
        self, value: Optional[Any], dialect: Dialect
    ) -> Optional[FileList]:
        if value is None:
            return FileList(files=[])
        if isinstance(value, list):
            return FileList(files=[File(**file) for file in value])
        raise TypeError(f"Expected list, got {type(value)}")


class Product(Base):
    __tablename__ = "product"
    __table_args__ = (
        CheckConstraint(
            "(csaf_product_id IS NULL) != (asset_id IS NULL)",
            name="check_exclusive_foreign_keys",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_type: Mapped[ProductType] = mapped_column(
        Enum(ProductType, name="product_type_enum"), default=ProductType.Undefined
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


class CsafProduct(Base, MetaInfo):
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
        result = {
            "origin_uri": self.origin_uri,
            "origin_info": self.origin_info,
            "last_update": self.last_update,
        }
        if self.id is not None:
            result["id"] = self.id
        return result


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


class Asset(Base, MetaInfo):
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
        result = {
            "origin_uri": self.origin_uri,
            "origin_info": self.origin_info,
            "last_update": self.last_update,
        }
        if self.id is not None:
            result["id"] = self.id
        return result


class Match(Base):
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    score: Mapped[float] = mapped_column(nullable=False)
    # TODO: Introduce enum for match status?
    status: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[datetime.datetime] = mapped_column(nullable=False)
    csaf_product_id: Mapped[int] = mapped_column(
        ForeignKey("cacheDB.csaf_product.id"), nullable=False
    )
    asset_id: Mapped[int] = mapped_column(
        ForeignKey("cacheDB.asset.id"), nullable=False
    )

    csaf_product: Mapped["CsafProduct"] = relationship(back_populates="matches")
    asset: Mapped["Asset"] = relationship(back_populates="matches")
