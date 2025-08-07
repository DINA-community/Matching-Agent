import datetime
import logging
from typing import List

from sqlalchemy import Float, ForeignKey, select

# from sqlalchemy.orm import selectinload
from sqlalchemy import Text, MetaData, Integer, JSON

# from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

logger = logging.getLogger(__name__)


class data_consistency_problem(Exception):
    """consistency with netbox data detected"""

    pass


class Base(AsyncAttrs, DeclarativeBase):
    metadata = MetaData(schema="cacheDB")


class AssetSynchronizer(Base):
    __tablename__ = "assetsync"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    last_run: Mapped[float] = mapped_column(Float)


class Manufacturer(Base):
    __tablename__ = "manufacturer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    last_seen: Mapped[float] = mapped_column(Float)
    name: Mapped[str] = mapped_column(Text)

    async def create_or_renew(
        self, session: AsyncSession, timestamp: float
    ) -> "Manufacturer":
        # Check if the asset already exists and is unchanged
        stmt = select(Manufacturer).where(
            Manufacturer.name == self.name,
        )
        result = await session.execute(stmt)

        if manufacturer := result.scalar_one_or_none():
            # We found an unchanged entry. Update the timestamp
            manufacturer.last_seen = timestamp
            logger.debug(
                f"Updated existing manufacturer {manufacturer.id} with timestamp {timestamp}"
            )
            return manufacturer
        else:
            # The asset has changed. We need to create a new entry for the updated version.
            self.last_seen = timestamp
            session.add(self)
            logger.debug("Created new manufacturer")
            return self


class DeviceType(Base):
    __tablename__ = "device_type"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nb_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    last_seen: Mapped[float] = mapped_column(Float)
    model: Mapped[str | None] = mapped_column(Text, nullable=True)
    model_number: Mapped[str | None] = mapped_column(Text, nullable=True)
    part_number: Mapped[str | None] = mapped_column(Text, nullable=True)
    device_family: Mapped[str | None] = mapped_column(Text, nullable=True)
    cpe: Mapped[str | None] = mapped_column(Text, nullable=True)
    hardware_version: Mapped[str | None] = mapped_column(Text, nullable=True)
    hardware_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    manufacturer_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.manufacturer.id"), nullable=True
    )

    manufacturer: Mapped["Manufacturer"] = relationship()

    async def create_or_renew(
        self, session: AsyncSession, timestamp: float
    ) -> "DeviceType":
        # First update the dependent objects. If they changed, we need to create a new asset.
        if self.manufacturer:
            self.manufacturer = await self.manufacturer.create_or_renew(
                session, timestamp
            )
            await session.flush()
            self.manufacturer_id = self.manufacturer.id

        # Check if the asset already exists and is unchanged
        stmt = select(DeviceType).where(
            DeviceType.nb_id == self.nb_id,
            DeviceType.model == self.model,
            DeviceType.model_number == self.model_number,
            DeviceType.part_number == self.part_number,
            DeviceType.device_family == self.device_family,
            DeviceType.cpe == self.cpe,
            DeviceType.hardware_version == self.hardware_version,
            DeviceType.hardware_name == self.hardware_name,
            DeviceType.manufacturer_id == self.manufacturer_id,
        )
        result = await session.execute(stmt)

        if device_type := result.scalar_one_or_none():
            # We found an unchanged entry. Update the timestamp
            device_type.last_seen = timestamp
            logger.debug(
                f"Updated existing device_type {device_type.id} with timestamp {timestamp}"
            )
            return device_type
        else:
            # The asset has changed. We need to create a new entry for the updated version.
            self.last_seen = timestamp
            session.add(self)
            logger.debug("Created new device_type")
            return self


class Software(Base):
    __tablename__ = "software"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nb_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    last_seen: Mapped[float] = mapped_column(Float)
    name: Mapped[str | None] = mapped_column(Text, nullable=True)
    version: Mapped[str | None] = mapped_column(Text, nullable=True)
    cpe: Mapped[str | None] = mapped_column(Text, nullable=True)
    purl: Mapped[str | None] = mapped_column(Text, nullable=True)
    sbom_urls: Mapped[List[str] | None] = mapped_column(JSON, nullable=True)
    manufacturer_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.manufacturer.id"), nullable=True
    )

    manufacturer: Mapped["Manufacturer"] = relationship()
    files: Mapped[List["File"]] = relationship()

    async def create_or_renew(
        self, session: AsyncSession, timestamp: float
    ) -> "Software":
        # First update the dependent objects. If they changed, we need to create a new asset.
        if await self.awaitable_attrs.manufacturer:
            self.manufacturer = await (
                await self.awaitable_attrs.manufacturer
            ).create_or_renew(session, timestamp)
            await session.flush()
            self.manufacturer_id = self.manufacturer.id

        # Check if the asset already exists and is unchanged
        stmt = select(Software).where(
            Software.nb_id == self.nb_id,
            Software.name == self.name,
            Software.version == self.version,
            Software.cpe == self.cpe,
            Software.purl == self.purl,
            Software.sbom_urls == self.sbom_urls,
            Software.manufacturer_id == self.manufacturer_id,
        )
        result = await session.execute(stmt)

        if software := result.scalar_one_or_none():
            # We found an unchanged entry. Update the timestamp
            software.last_seen = timestamp
            logger.debug(
                f"Updated existing software {software.id} with timestamp {timestamp}"
            )
            return software
        else:
            # The asset has changed. We need to create a new entry for the updated version.
            self.last_seen = timestamp
            session.add(self)
            logger.debug("Created new software")
            return self


class Device(Base):
    __tablename__ = "device"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nb_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    last_seen: Mapped[float] = mapped_column(Float)
    name: Mapped[str | None] = mapped_column(Text, nullable=True)
    serial: Mapped[str | None] = mapped_column(Text, nullable=True)
    device_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.device_type.id"), nullable=True
    )

    device_type: Mapped["DeviceType"] = relationship()

    async def create_or_renew(
        self, session: AsyncSession, timestamp: float
    ) -> "Device":
        # First update the dependent objects. If they changed, we need to create a new asset.
        if self.device_type:
            self.device_type = await self.device_type.create_or_renew(
                session, timestamp
            )
            await session.flush()
            self.device_type_id = self.device_type.id

        # Check if the asset already exists and is unchanged
        stmt = select(Device).where(
            Device.nb_id == self.nb_id,
            Device.name == self.name,
            Device.serial == self.serial,
            Device.device_type_id == self.device_type_id,
        )
        result = await session.execute(stmt)

        if device := result.scalar_one_or_none():
            # We found an unchanged entry. Update the timestamp
            device.last_seen = timestamp
            logger.debug(
                f"Updated existing device {device.id} with timestamp {timestamp}"
            )
            return device
        else:
            # The asset has changed. We need to create a new entry for the updated version.
            self.last_seen = timestamp
            session.add(self)
            logger.debug("Created new device")
            return self


class Asset(Base):
    __tablename__ = "asset"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    last_seen: Mapped[float] = mapped_column(Float)
    device_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.device.id"), nullable=True
    )
    software_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.software.id"), nullable=True
    )

    device: Mapped["Device"] = relationship()
    software: Mapped["Software"] = relationship()

    async def create_or_renew(self, session: AsyncSession, timestamp: float) -> "Asset":
        # First update the dependent objects. If they changed, we need to create a new asset.
        if self.device:
            self.device = await self.device.create_or_renew(session, timestamp)
        if self.software:
            self.software = await self.software.create_or_renew(session, timestamp)
        await session.flush()
        if self.device:
            self.device_id = self.device.id
        if self.software:
            self.software_id = self.software.id

        # Check if the asset already exists and is unchanged
        stmt = select(Asset).where(
            Asset.device_id == self.device_id, Asset.software_id == self.software_id
        )
        result = await session.execute(stmt)

        if asset := result.scalar_one_or_none():
            # We found an unchanged entry. Update the timestamp
            asset.last_seen = timestamp
            logger.debug(
                f"Updated existing asset {asset.id} with timestamp {timestamp}"
            )
            return asset
        else:
            # The asset has changed. We need to create a new entry for the updated version.
            self.last_seen = timestamp
            session.add(self)
            logger.debug("Created new asset")
            return self


class ProductRelationship(Base):
    __tablename__ = "productrelationship"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nb_id: Mapped[int] = mapped_column(Integer)
    last_seen: Mapped[float] = mapped_column(Float)
    nb_source_id: Mapped[int] = mapped_column(Integer)
    nb_target_id: Mapped[int] = mapped_column(Integer)
    category: Mapped[int] = mapped_column(Integer)
    source_id: Mapped[int] = mapped_column(Integer)
    source_type: Mapped[str] = mapped_column(Text)
    target_id: Mapped[int] = mapped_column(Integer)
    target_type: Mapped[str] = mapped_column(Text)

    def get_source(self, session):
        if self.source_type == "Device":
            return session.get(Device, self.source_id)
        elif self.source_type == "Software":
            return session.get(Software, self.source_id)
        else:
            return None

    def get_target(self, session):
        if self.target_type == "Device":
            return session.get(Device, self.target_id)
        elif self.target_type == "Software":
            return session.get(Software, self.target_id)
        else:
            return None


class File(Base):
    __tablename__ = "file"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nb_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    last_seen: Mapped[float] = mapped_column(Float)
    nb_software_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    filename: Mapped[str | None] = mapped_column(Text, nullable=True)
    software_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.software.id"), nullable=True
    )

    hashes: Mapped[List["Hash"]] = relationship(back_populates="file")


class Hash(Base):
    __tablename__ = "hash"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nb_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    last_seen: Mapped[float] = mapped_column(Float)
    nb_file_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    algorithm: Mapped[str | None] = mapped_column(Text, nullable=True)
    value: Mapped[str | None] = mapped_column(Text, nullable=True)
    file_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.file.id"), nullable=True
    )

    file: Mapped["File"] = relationship(back_populates="hashes")


class CsafDocument(Base):
    __tablename__ = "csaf_document"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    url: Mapped[str | None] = mapped_column(Text, nullable=True)
    title: Mapped[str | None] = mapped_column(Text, nullable=True)
    version: Mapped[str | None] = mapped_column(Text, nullable=True)
    lang: Mapped[str | None] = mapped_column(Text, nullable=True)
    publisher: Mapped[str | None] = mapped_column(Text, nullable=True)

    csaf_product_trees: Mapped[List["CsafProductTree"]] = relationship(
        back_populates="csaf_document"
    )

    async def create_or_renew(
        self, session: AsyncSession, timestamp: float
    ) -> "CsafDocument":
        return self


class CsafProduct(Base):
    __tablename__ = "csaf_product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    device_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.device.id"), nullable=True
    )
    software_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.software.id"), nullable=True
    )

    device: Mapped["Device"] = relationship()
    software: Mapped["Software"] = relationship()
    csaf_product_trees: Mapped[List["CsafProductTree"]] = relationship(
        back_populates="csaf_product"
    )


class CsafProductTree(Base):
    __tablename__ = "csaf_product_tree"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    csaf_document_id: Mapped[int] = mapped_column(
        ForeignKey("cacheDB.csaf_document.id")
    )
    csaf_product_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.csaf_product.id"))

    csaf_document: Mapped["CsafDocument"] = relationship(
        back_populates="csaf_product_trees"
    )
    csaf_product: Mapped["CsafProduct"] = relationship(
        back_populates="csaf_product_trees"
    )


class Match(Base):
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    score: Mapped[float]
    status: Mapped[str] = mapped_column(Text)
    time: Mapped[datetime.datetime]

    csaf_product_tree_id: Mapped[int] = mapped_column(
        ForeignKey("cacheDB.csaf_product_tree.id")
    )
    asset_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.asset.id"))

    csaf_product_tree: Mapped["CsafProductTree"] = relationship()
    asset: Mapped["Asset"] = relationship()
