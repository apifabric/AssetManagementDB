# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Device(Base):
    """
    description: Stores information about IT devices in the system.
    """
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    manufacturer = Column(String)
    model = Column(String)
    purchase_date = Column(Date)
    warranty_expiry = Column(Date)


class Software(Base):
    """
    description: Contains details about software available in the system.
    """
    __tablename__ = 'software'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    version = Column(String)
    license_expiry = Column(Date)
    vendor = Column(String)


class Location(Base):
    """
    description: Represents the physical location or premises related to assets.
    """
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    address = Column(String)
    country = Column(String)


class AssetManagementLog(Base):
    """
    description: Log of asset movement and status changes.
    """
    __tablename__ = 'asset_management_log'

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('device.id'))
    from_location_id = Column(Integer, ForeignKey('location.id'))
    to_location_id = Column(Integer, ForeignKey('location.id'))
    log_date = Column(Date)
    activity = Column(String)


class Employee(Base):
    """
    description: Contains employee details.
    """
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    position = Column(String)
    email = Column(String)


class DeviceAssignment(Base):
    """
    description: Track which employee has been assigned to a device.
    """
    __tablename__ = 'device_assignment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    device_id = Column(Integer, ForeignKey('device.id'))
    start_date = Column(Date)
    end_date = Column(Date)


class MaintenanceSchedule(Base):
    """
    description: Planned maintenance for devices.
    """
    __tablename__ = 'maintenance_schedule'

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('device.id'))
    scheduled_date = Column(Date)
    description = Column(String)


class VendorContract(Base):
    """
    description: Details of vendor contracts.
    """
    __tablename__ = 'vendor_contract'

    id = Column(Integer, primary_key=True, autoincrement=True)
    vendor_name = Column(String)
    contract_start = Column(Date)
    contract_end = Column(Date)
    terms = Column(String)


class DeviceSoftware(Base):
    """
    description: Links devices with software installations.
    """
    __tablename__ = 'device_software'

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('device.id'))
    software_id = Column(Integer, ForeignKey('software.id'))
    installation_date = Column(Date)


class ComplianceAudit(Base):
    """
    description: Records audits for compliance tracking.
    """
    __tablename__ = 'compliance_audit'

    id = Column(Integer, primary_key=True, autoincrement=True)
    audit_date = Column(Date)
    findings = Column(String)
    auditor = Column(String)


class WarrantyService(Base):
    """
    description: Manages details of warranty services for devices.
    """
    __tablename__ = 'warranty_service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('device.id'))
    vendor_contract_id = Column(Integer, ForeignKey('vendor_contract.id'))
    service_date = Column(Date)
    service_notes = Column(String)


class RenewalAlert(Base):
    """
    description: Manages renewal alerts for software licenses and contracts.
    """
    __tablename__ = 'renewal_alert'

    id = Column(Integer, primary_key=True, autoincrement=True)
    alert_date = Column(Date)
    entity_type = Column(String)
    entity_id = Column(Integer)
    message = Column(String)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    device1 = Device(name="Workstation A", manufacturer="Dell", model="Optiplex 7070", purchase_date=date(2020, 5, 15), warranty_expiry=date(2023, 5, 15))
    device2 = Device(name="Laptop B", manufacturer="HP", model="Pavilion 15", purchase_date=date(2021, 7, 22), warranty_expiry=date(2024, 7, 22))
    device3 = Device(name="Printer C", manufacturer="Brother", model="HL-L2350DW", purchase_date=date(2019, 10, 1), warranty_expiry=date(2022, 10, 1))
    device4 = Device(name="Server D", manufacturer="IBM", model="Power9", purchase_date=date(2018, 9, 30), warranty_expiry=date(2023, 9, 30))
    
    
    
    session.add_all([device1, device2, device3, device4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
