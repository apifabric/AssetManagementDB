# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  December 23, 2024 20:34:20
# Database: sqlite:////tmp/tmp.YJC797K874-01JFTKF18CBNB6WD530X8E3K9F/ECommerceModel/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class ComplianceAudit(SAFRSBaseX, Base):
    """
    description: Records audits for compliance tracking.
    """
    __tablename__ = 'compliance_audit'
    _s_collection_name = 'ComplianceAudit'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    audit_date = Column(Date)
    findings = Column(String)
    auditor = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Device(SAFRSBaseX, Base):
    """
    description: Stores information about IT devices in the system.
    """
    __tablename__ = 'device'
    _s_collection_name = 'Device'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    manufacturer = Column(String)
    model = Column(String)
    purchase_date = Column(Date)
    warranty_expiry = Column(Date)

    # parent relationships (access parent)

    # child relationships (access children)
    AssetManagementLogList : Mapped[List["AssetManagementLog"]] = relationship(back_populates="device")
    DeviceAssignmentList : Mapped[List["DeviceAssignment"]] = relationship(back_populates="device")
    DeviceSoftwareList : Mapped[List["DeviceSoftware"]] = relationship(back_populates="device")
    MaintenanceScheduleList : Mapped[List["MaintenanceSchedule"]] = relationship(back_populates="device")
    WarrantyServiceList : Mapped[List["WarrantyService"]] = relationship(back_populates="device")



class Employee(SAFRSBaseX, Base):
    """
    description: Contains employee details.
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    position = Column(String)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    DeviceAssignmentList : Mapped[List["DeviceAssignment"]] = relationship(back_populates="employee")



class Location(SAFRSBaseX, Base):
    """
    description: Represents the physical location or premises related to assets.
    """
    __tablename__ = 'location'
    _s_collection_name = 'Location'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    country = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    AssetManagementLogList : Mapped[List["AssetManagementLog"]] = relationship(foreign_keys='[AssetManagementLog.from_location_id]', back_populates="from_location")
    toAssetManagementLogList : Mapped[List["AssetManagementLog"]] = relationship(foreign_keys='[AssetManagementLog.to_location_id]', back_populates="to_location")



class RenewalAlert(SAFRSBaseX, Base):
    """
    description: Manages renewal alerts for software licenses and contracts.
    """
    __tablename__ = 'renewal_alert'
    _s_collection_name = 'RenewalAlert'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    alert_date = Column(Date)
    entity_type = Column(String)
    entity_id = Column(Integer)
    message = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Software(SAFRSBaseX, Base):
    """
    description: Contains details about software available in the system.
    """
    __tablename__ = 'software'
    _s_collection_name = 'Software'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    version = Column(String)
    license_expiry = Column(Date)
    vendor = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    DeviceSoftwareList : Mapped[List["DeviceSoftware"]] = relationship(back_populates="software")



class VendorContract(SAFRSBaseX, Base):
    """
    description: Details of vendor contracts.
    """
    __tablename__ = 'vendor_contract'
    _s_collection_name = 'VendorContract'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    vendor_name = Column(String)
    contract_start = Column(Date)
    contract_end = Column(Date)
    terms = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    WarrantyServiceList : Mapped[List["WarrantyService"]] = relationship(back_populates="vendor_contract")



class AssetManagementLog(SAFRSBaseX, Base):
    """
    description: Log of asset movement and status changes.
    """
    __tablename__ = 'asset_management_log'
    _s_collection_name = 'AssetManagementLog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    device_id = Column(ForeignKey('device.id'))
    from_location_id = Column(ForeignKey('location.id'))
    to_location_id = Column(ForeignKey('location.id'))
    log_date = Column(Date)
    activity = Column(String)

    # parent relationships (access parent)
    device : Mapped["Device"] = relationship(back_populates=("AssetManagementLogList"))
    from_location : Mapped["Location"] = relationship(foreign_keys='[AssetManagementLog.from_location_id]', back_populates=("AssetManagementLogList"))
    to_location : Mapped["Location"] = relationship(foreign_keys='[AssetManagementLog.to_location_id]', back_populates=("toAssetManagementLogList"))

    # child relationships (access children)



class DeviceAssignment(SAFRSBaseX, Base):
    """
    description: Track which employee has been assigned to a device.
    """
    __tablename__ = 'device_assignment'
    _s_collection_name = 'DeviceAssignment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey('employee.id'))
    device_id = Column(ForeignKey('device.id'))
    start_date = Column(Date)
    end_date = Column(Date)

    # parent relationships (access parent)
    device : Mapped["Device"] = relationship(back_populates=("DeviceAssignmentList"))
    employee : Mapped["Employee"] = relationship(back_populates=("DeviceAssignmentList"))

    # child relationships (access children)



class DeviceSoftware(SAFRSBaseX, Base):
    """
    description: Links devices with software installations.
    """
    __tablename__ = 'device_software'
    _s_collection_name = 'DeviceSoftware'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    device_id = Column(ForeignKey('device.id'))
    software_id = Column(ForeignKey('software.id'))
    installation_date = Column(Date)

    # parent relationships (access parent)
    device : Mapped["Device"] = relationship(back_populates=("DeviceSoftwareList"))
    software : Mapped["Software"] = relationship(back_populates=("DeviceSoftwareList"))

    # child relationships (access children)



class MaintenanceSchedule(SAFRSBaseX, Base):
    """
    description: Planned maintenance for devices.
    """
    __tablename__ = 'maintenance_schedule'
    _s_collection_name = 'MaintenanceSchedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    device_id = Column(ForeignKey('device.id'))
    scheduled_date = Column(Date)
    description = Column(String)

    # parent relationships (access parent)
    device : Mapped["Device"] = relationship(back_populates=("MaintenanceScheduleList"))

    # child relationships (access children)



class WarrantyService(SAFRSBaseX, Base):
    """
    description: Manages details of warranty services for devices.
    """
    __tablename__ = 'warranty_service'
    _s_collection_name = 'WarrantyService'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    device_id = Column(ForeignKey('device.id'))
    vendor_contract_id = Column(ForeignKey('vendor_contract.id'))
    service_date = Column(Date)
    service_notes = Column(String)

    # parent relationships (access parent)
    device : Mapped["Device"] = relationship(back_populates=("WarrantyServiceList"))
    vendor_contract : Mapped["VendorContract"] = relationship(back_populates=("WarrantyServiceList"))

    # child relationships (access children)
