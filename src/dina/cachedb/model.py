import datetime
import logging
from sqlalchemy import Text, ForeignKey, MetaData, Integer, JSON, Float
from sqlalchemy.ext.asyncio import AsyncAttrs
from typing import List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
#from sqlalchemy.orm import selectinload
from sqlalchemy import Text, ForeignKey, MetaData, Integer, JSON

from sqlalchemy import select

logger = logging.getLogger(__name__)

class data_consistency_problem(Exception):
    """consistency with netbox data detected"""
    pass

class Base(AsyncAttrs, DeclarativeBase):
    metadata = MetaData(schema="cacheDB")
    pass

class AssetSynchronizer(Base):
    __tablename__ = "assetsync"
    id: Mapped[int] = mapped_column(primary_key=True)
    last_run: Mapped[float] = mapped_column(Float)

    async def create_or_update(self, session) -> None:
        stmt = select(AssetSynchronizer)
        result = await session.execute(stmt)
        obj = result.scalar_one_or_none()
        if obj:
            setattr(obj, "last_run", self.last_run)
        else:
            session.add(self)
        return obj

class Manufacturer(Base):
    __tablename__ = "manufacturer"

    id: Mapped[int] = mapped_column(primary_key=True)
    nb_id: Mapped[int] = mapped_column(Integer)
    last_seen: Mapped[float] = mapped_column(Float)
    name: Mapped[str] = mapped_column(Text)

    device_types: Mapped[List["DeviceType"]] = relationship(
        back_populates="manufacturer"
    )
    software: Mapped[List["Software"]] = relationship(back_populates="manufacturer")

    async def create_or_update(self, session) -> None:
        updated = False
        stmt = select(Manufacturer).where(Manufacturer.nb_id == self.nb_id)
        #stmt = select(Manufacturer).options(selectinload(Manufacturer.device_types)).options(selectinload(Manufacturer.software)).where(
        #    Manufacturer.nb_id == self.nb_id)
        result = await session.execute(stmt)
        obj = result.scalar_one_or_none()
        if obj:
            if obj.name != self.name:
                setattr(obj, "name", self.name)
                updated = True
            setattr(obj, "last_seen", self.last_seen)
            if updated:
                logger.info(f"UPDATED: {self} {self.name}")
        else:
            session.add(self)
            logger.info(f"CREATED: {self} {self.name}")
        return obj

class DeviceType(Base):
    __tablename__ = "device_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    nb_id: Mapped[int] = mapped_column(Integer)
    last_seen: Mapped[float] = mapped_column(Float)
    nb_manu_id: Mapped[int] = mapped_column(Integer)
    model: Mapped[str] = mapped_column(Text)
    model_number: Mapped[str | None] = mapped_column(Text)
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

    async def create_or_update(self, session) -> None:
        updated = False
        async def find_manufacturer_key(nb_key):
            stmt = select(Manufacturer).where(Manufacturer.nb_id == nb_key)
            result = await session.execute(stmt)
            obj = result.scalar_one_or_none()
            if obj:
                return obj.id
            else:
                raise data_consistency_problem("Manufacturer not found")

        stmt = select(DeviceType).where(DeviceType.nb_id == self.nb_id)
        result = await session.execute(stmt)
        obj = result.scalar_one_or_none()
        manu_id = await find_manufacturer_key(self.nb_manu_id)
        if obj:
            if obj.model_number != self.model_number:
                setattr(obj, "model_number", self.model_number)
                updated = True
            if obj.part_number != self.part_number:
                setattr(obj, "part_number", self.part_number)
            if obj.device_family != self.device_family:
                setattr(obj, "device_family", self.device_family)
                updated = True
            if obj.cpe != self.cpe:
                setattr(obj, "cpe", self.cpe)
                updated = True
            if obj.hardware_version != self.hardware_version:
                setattr(obj, "hardware_version", self.hardware_version)
                updated = True
            if obj.hardware_name != self.hardware_name:
                setattr(obj, "hardware_name", self.hardware_name)
                updated = True
            if obj.manufacturer_id != manu_id:
                setattr(obj, "manufacturer_id", manu_id)
                updated = True
            setattr(obj, "last_seen", self.last_seen)
            if updated:
                logger.info(f"UPDATED: {self} {self.model_number}")
        else:
            self.manufacturer_id = manu_id
            session.add(self)
            logger.info(f"CREATED: {self} {self.model_number}")
        return obj

class Software(Base):
    __tablename__ = "software"

    id: Mapped[int] = mapped_column(primary_key=True)
    nb_id: Mapped[int] = mapped_column(Integer)
    last_seen: Mapped[float] = mapped_column(Float)
    nb_manu_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(Text)
    version: Mapped[str | None] = mapped_column(Text)
    cpe: Mapped[str | None] = mapped_column(Text)
    purl: Mapped[str | None] = mapped_column(Text)
    sbom_urls: Mapped[List[ str ]| None] = mapped_column(JSON)
    manufacturer_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.manufacturer.id")
    )

    manufacturer: Mapped["Manufacturer"] = relationship(back_populates="software")
    assets: Mapped[List["Asset"]] = relationship(back_populates="software")
    files: Mapped[List["File"]] = relationship(back_populates="software")
    csaf_products: Mapped[List["CsafProduct"]] = relationship(back_populates="software")

    async def create_or_update(self, session) -> None:
        updated = False
        async def find_manufacturer_key(nb_key):
            stmt = select(Manufacturer).where(Manufacturer.nb_id == nb_key)
            result = await session.execute(stmt)
            obj = result.scalar_one_or_none()
            if obj:
                return obj.id
            else:
                raise data_consistency_problem("Manufacturer not found")

        stmt = select(Software).where(Software.nb_id == self.nb_id)
        result = await session.execute(stmt)
        obj = result.scalar_one_or_none()
        manu_id = await find_manufacturer_key(self.nb_manu_id)
        if obj:
            if obj.name != self.name:
                setattr(obj, "name", self.name)
                updated = True
            if obj.version != self.version:
                setattr(obj, "version", self.version)
                updated = True
            if obj.cpe != self.cpe:
                setattr(obj, "cpe", self.cpe)
                updated = True
            if obj.purl != self.purl:
                setattr(obj, "purl", self.purl)
                updated = True
            if obj.sbom_urls != self.sbom_urls:
                setattr(obj, "sbom_urls", self.sbom_urls)
                updated = True
            if obj.manufacturer_id != manu_id:
                setattr(obj, "manufacturer_id", manu_id)
                updated = True
            setattr(obj, "last_seen", self.last_seen)
            if updated:
                logger.info(f"UPDATED: {self} {self.name}")
        else:
            self.manufacturer_id = manu_id
            session.add(self)
            await session.flush()
            the_asset = Asset(software_id=self.id,last_seen=self.last_seen)
            session.add(the_asset)
            logger.info(f"CREATED: {self} {self.name}")
            logger.info(f"CREATED: {the_asset} {the_asset.id}")
        return obj

class Device(Base):
    __tablename__ = "device"

    id: Mapped[int] = mapped_column(primary_key=True)
    nb_id: Mapped[int] = mapped_column(Integer)
    last_seen: Mapped[float] = mapped_column(Float)
    nb_devicetype_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str | None] = mapped_column(Text)
    serial: Mapped[str | None] = mapped_column(Text)
    device_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("cacheDB.device_type.id")
    )

    device_type: Mapped["DeviceType"] = relationship(back_populates="devices")
    assets: Mapped[List["Asset"]] = relationship(back_populates="device")
    csaf_products: Mapped[List["CsafProduct"]] = relationship(back_populates="device")

    async def create_or_update(self, session) -> None:
        updated = False
        async def find_devicetype_key(nb_key):
            stmt = select(DeviceType).where(DeviceType.nb_id == nb_key)
            result = await session.execute(stmt)
            obj = result.scalar_one_or_none()
            if obj:
                return obj.id
            else:
                raise data_consistency_problem("DeviceType not found")

        stmt = select(Device).where(Device.nb_id == self.nb_id)
        result = await session.execute(stmt)
        obj = result.scalar_one_or_none()
        devicetype_id = await find_devicetype_key(self.nb_devicetype_id)
        if obj:
            if obj.name != self.name:
                setattr(obj, "name", self.name)
                updated = True
            if obj.serial != self.serial:
                setattr(obj, "serial", self.serial)
                updated = True
            if obj.device_type_id != devicetype_id:
                setattr(obj, "device_type_id", devicetype_id)
                updated = True
            setattr(obj, "last_seen", self.last_seen)
            if updated:
                logger.info(f"UPDATED: {self} {self.name}")
        else:
            self.device_type_id = devicetype_id
            session.add(self)
            await session.flush()
            the_asset = Asset(device_id=self.id,last_seen=self.last_seen)
            session.add(the_asset)
            logger.info(f"CREATED: {self} {self.name}")
            logger.info(f"CREATED: {the_asset} {the_asset.id}")
        return obj

class Asset(Base):
    __tablename__ = "asset"

    id: Mapped[int] = mapped_column(primary_key=True)
    last_seen: Mapped[float] = mapped_column(Float)
    device_id: Mapped[int | None] = mapped_column(ForeignKey("cacheDB.device.id"))
    software_id: Mapped[int | None] = mapped_column(ForeignKey("cacheDB.software.id"))

    device: Mapped["Device"] = relationship(back_populates="assets")
    software: Mapped["Software"] = relationship(back_populates="assets")
    matches: Mapped[List["Match"]] = relationship(back_populates="asset")


class ProductRelationship(Base):
    __tablename__ = "productrelationship"

    id: Mapped[int] = mapped_column(primary_key=True)
    nb_id: Mapped[int] = mapped_column(Integer)
    last_seen: Mapped[float] = mapped_column(Float)
    nb_source_id: Mapped[int] = mapped_column(Integer)
    nb_target_id: Mapped[int] = mapped_column(Integer)
    category: Mapped[int] = mapped_column(Integer)
    source_id: Mapped[int] = mapped_column(Integer)
    source_type: Mapped[str] = mapped_column(Text)
    target_id: Mapped[int] = mapped_column(Integer)
    target_type: Mapped[str] = mapped_column(Text)

    def get_source(self,session):
        if self.source_type == 'Device':
            return session.get(Device, self.source_id)
        elif self.source_type == 'Software':
            return session.get(Software, self.source_id)
        else:
            return None

    def get_target(self,session):
        if self.target_type == 'Device':
            return session.get(Device, self.target_id)
        elif self.target_type == 'Software':
            return session.get(Software, self.target_id)
        else:
            return None

    async def create_or_update(self, session) -> None:
        updated = False
        async def find_related_key(nb_key, the_type):
            if the_type == 'Device':
                stmt = select(Device).where(Device.nb_id == nb_key)
            elif the_type == 'Software':
                stmt = select(Software).where(Software.nb_id == nb_key)
            else:
                return None
            result = await session.execute(stmt)
            obj = result.scalar_one_or_none()
            if obj:
                return obj.id
            else:
                raise data_consistency_problem("Device of Software not found")

        stmt = select(ProductRelationship).where(ProductRelationship.nb_id == self.nb_id)
        result = await session.execute(stmt)
        obj = result.scalar_one_or_none()
        source_id = await find_related_key(self.nb_source_id, self.source_type)
        target_id = await find_related_key(self.nb_target_id, self.target_type)
        if obj:
            if obj.source_id != source_id:
                setattr(obj, "source_id", source_id)
                updated = True
            if obj.target_id != target_id:
                setattr(obj, "target_id", target_id)
                updated = True
            if obj.source_type != self.source_type:
                setattr(obj, "source_type", self.source_type)
                updated = True
            if obj.target_type != self.target_type:
                setattr(obj, "target_type", self.target_type)
                updated = True
            if obj.category != self.category:
                setattr(obj, "category", self.category)
                updated = True
            setattr(obj, "last_seen", self.last_seen)
            if updated:
                logger.info(f"UPDATED: {self}")
        else:
            self.source_id = source_id
            self.target_id = target_id
            session.add(self)
            logger.info(f"CREATED: {self} {self.id}")
        return obj

class File(Base):
    __tablename__ = "file"

    id: Mapped[int] = mapped_column(primary_key=True)
    nb_id: Mapped[int] = mapped_column(Integer)
    last_seen: Mapped[float] = mapped_column(Float)
    nb_software_id: Mapped[int] = mapped_column(Integer)
    filename: Mapped[str]
    software_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.software.id"))

    software: Mapped["Software"] = relationship(back_populates="files")
    hashes: Mapped[List["Hash"]] = relationship(back_populates="file")

    async def create_or_update(self, session) -> None:
        updated = False
        async def find_software_key(nb_key):
            stmt = select(Software).where(Software.nb_id == nb_key)
            result = await session.execute(stmt)
            obj = result.scalar_one_or_none()
            if obj:
                return(obj.id)
            else:
                raise data_consistency_problem("Software not found")

        stmt = select(File).where(File.nb_id == self.nb_id)
        result = await session.execute(stmt)
        obj = result.scalar_one_or_none()
        software_id = await find_software_key(self.nb_software_id)
        if obj:
            if obj.filename != self.filename:
                setattr(obj, "filename", self.filename)
                updated = True
            if obj.software_id != software_id:
                setattr(obj, "software_id", software_id)
                updated = True
            setattr(obj, "last_seen", self.last_seen)
            if updated:
                logger.info(f"UPDATED: {self} {self.filename}")
        else:
            self.software_id = software_id
            session.add(self)
            logger.info(f"CREATED: {self} {self.filename}")
        return obj

class Hash(Base):
    __tablename__ = "hash"

    id: Mapped[int] = mapped_column(primary_key=True)
    nb_id: Mapped[int] = mapped_column(Integer)
    last_seen: Mapped[float] = mapped_column(Float)
    nb_file_id: Mapped[int] = mapped_column(Integer)
    algorithm: Mapped[str] = mapped_column(Text)
    value: Mapped[str] = mapped_column(Text)
    file_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.file.id"))

    file: Mapped["File"] = relationship(back_populates="hashes")

    async def create_or_update(self, session) -> None:
        updated = False
        async def find_file_key(nb_key):
            stmt = select(File).where(File.nb_id == nb_key)
            result = await session.execute(stmt)
            obj = result.scalar_one_or_none()
            if obj:
                return obj.id
            else:
                raise data_consistency_problem("File not found")

        stmt = select(Hash).where(Hash.nb_id == self.nb_id)
        result = await session.execute(stmt)
        obj = result.scalar_one_or_none()
        file_id = await find_file_key(self.nb_file_id)
        if obj:
            #logger.info(f"FOUND: {obj.nb_id} {obj.name}")
            if obj.algorithm != self.algorithm:
                setattr(obj, "algorithm", self.name)
                updated = True
            if obj.value != self.value:
                setattr(obj, "value", self.serial)
                updated = True
            if obj.file_id != file_id:
                setattr(obj, "file_id", file_id)
                updated = True
            setattr(obj, "last_seen", self.last_seen)
            if updated:
                logger.info(f"UPDATED: {self} {self.id}")
        else:
            self.file_id = file_id
            session.add(self)
            logger.info(f"CREATED: {self} {self.id}")
        return obj

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

    id: Mapped[int] = mapped_column(primary_key=True)
    score: Mapped[float]
    status: Mapped[str] = mapped_column(Text)
    time: Mapped[datetime.datetime]
    csaf_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.csaf_document.id"))
    asset_id: Mapped[int] = mapped_column(ForeignKey("cacheDB.asset.id"))

    csaf_document: Mapped["CsafDocument"] = relationship(back_populates="matches")
    asset: Mapped["Asset"] = relationship(back_populates="matches")
