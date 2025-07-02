import datetime

from sqlalchemy import Text, ForeignKey, MetaData
from sqlalchemy.ext.asyncio import AsyncAttrs
from typing import List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(AsyncAttrs, DeclarativeBase):
    metadata = MetaData(schema="cacheDB")
    pass


class Manufacturer(Base):
    __tablename__ = "manufacturer"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text)

    device_types: Mapped[List["DeviceType"]] = relationship(
        back_populates="manufacturer"
    )
    software: Mapped[List["Software"]] = relationship(back_populates="manufacturer")


class DeviceType(Base):
    __tablename__ = "device_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    model_number: Mapped[str] = mapped_column(Text)
    part_number: Mapped[str | None] = mapped_column(Text)
    device_family: Mapped[str | None] = mapped_column(Text)
    cpe: Mapped[str | None] = mapped_column(Text)
    hardware_version: Mapped[str | None] = mapped_column(Text)
    hardware_name: Mapped[str | None] = mapped_column(Text)
    manufacturer_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.manufacturer.id")
    )

    manufacturer: Mapped["Manufacturer"] = relationship(back_populates="device_types")
    devices: Mapped[List["Device"]] = relationship(back_populates="device_type")


class Software(Base):
    __tablename__ = "software"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    version: Mapped[str | None] = mapped_column(Text)
    cpe: Mapped[str | None] = mapped_column(Text)
    purl: Mapped[str | None] = mapped_column(Text)
    sbom_urls: Mapped[str | None] = mapped_column(Text)
    manufacturer_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.manufacturer.id")
    )

    manufacturer: Mapped["Manufacturer"] = relationship(back_populates="software")
    assets: Mapped[List["Asset"]] = relationship(back_populates="software")
    files: Mapped[List["File"]] = relationship(back_populates="software")
    csaf_products: Mapped[List["CsafProduct"]] = relationship(back_populates="software")


class Device(Base):
    __tablename__ = "device"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column(Text)
    serial: Mapped[str | None] = mapped_column(Text)
    device_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.device_type.id")
    )

    device_type: Mapped["DeviceType"] = relationship(back_populates="devices")
    assets: Mapped[List["Asset"]] = relationship(back_populates="device")
    csaf_products: Mapped[List["CsafProduct"]] = relationship(back_populates="device")


class Asset(Base):
    __tablename__ = "asset"

    id: Mapped[int] = mapped_column(primary_key=True)
    device_id: Mapped[int | None] = mapped_column(ForeignKey("cacheDB.device.id"))
    software_id: Mapped[int | None] = mapped_column(ForeignKey("cacheDB.software.id"))

    device: Mapped["Device"] = relationship(back_populates="assets")
    software: Mapped["Software"] = relationship(back_populates="assets")
    matches: Mapped[List["Match"]] = relationship(back_populates="asset")


class File(Base):
    __tablename__ = "file"

    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str]
    software_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.software.id"))

    software: Mapped["Software"] = relationship(back_populates="files")
    hashes: Mapped[List["Hash"]] = relationship(back_populates="file")


class Hash(Base):
    __tablename__ = "hash"

    id: Mapped[int] = mapped_column(primary_key=True)
    algorithm: Mapped[str] = mapped_column(Text)
    value: Mapped[str] = mapped_column(Text)
    file_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.file.id"))

    file: Mapped["File"] = relationship(back_populates="hashes")


class CsafDocument(Base):
    __tablename__ = "csaf_document"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(Text)
    title: Mapped[str] = mapped_column(Text)
    version: Mapped[str] = mapped_column(Text)
    lang: Mapped[str]
    publisher: Mapped[str | None] = mapped_column(Text)

    matches: Mapped[List["Match"]] = relationship(back_populates="csaf_document")
    csaf_product_trees: Mapped[List["CsafProductTree"]] = relationship(
        back_populates="csaf_document"
    )


class CsafProduct(Base):
    __tablename__ = "csaf_product"

    id: Mapped[int] = mapped_column(primary_key=True)
    device_id: Mapped[int | None] = mapped_column(ForeignKey("cacheDB.device.id"))
    software_id: Mapped[int | None] = mapped_column(ForeignKey("cacheDB.software.id"))

    device: Mapped["Device"] = relationship(back_populates="csaf_products")
    software: Mapped["Software"] = relationship(back_populates="csaf_products")
    csaf_product_trees: Mapped[List["CsafProductTree"]] = relationship(
        back_populates="csaf_product"
    )


class CsafProductTree(Base):
    __tablename__ = "csaf_product_tree"

    id: Mapped[str] = mapped_column(primary_key=True)
    csaf_document_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.csaf_document.id"))
    csaf_product_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.csaf_product.id"))

    csaf_document: Mapped["CsafDocument"] = relationship(
        back_populates="csaf_product_trees"
    )
    csaf_product: Mapped["CsafProduct"] = relationship(
        back_populates="csaf_product_trees"
    )


class Match(Base):
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(primary_key=True)
    score: Mapped[float]
    status: Mapped[str] = mapped_column(Text)
    time: Mapped[datetime.datetime]
    csaf_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.csaf_document.id"))
    asset_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.asset.id"))

    csaf_document: Mapped["CsafDocument"] = relationship(back_populates="matches")
    asset: Mapped["Asset"] = relationship(back_populates="matches")
