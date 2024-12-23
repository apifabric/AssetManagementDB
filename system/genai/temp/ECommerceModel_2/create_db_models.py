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


class Device(Base):\n    \n    __tablename__ = 'device'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))\n    purchase_date = Column(DateTime)\n    warranty_period = Column(Integer)\n    price = Column(Integer)


class Manufacturer(Base):\n\n    __tablename__ = 'manufacturer'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    contact_email = Column(String)\n    phone_number = Column(String)


class Component(Base):\n\n    __tablename__ = 'component'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    device_id = Column(Integer, ForeignKey('device.id'))\n    component_type = Column(String, nullable=False)\n    description = Column(String)\n    serial_number = Column(String)


class MaintenanceRecord(Base):\n\n    __tablename__ = 'maintenance_record'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    device_id = Column(Integer, ForeignKey('device.id'))\n    maintenance_date = Column(DateTime)\n    summary = Column(String)\n    cost = Column(Integer)


class User(Base):\n\n    __tablename__ = 'user'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    username = Column(String, nullable=False)\n    email = Column(String)\n    password_hash = Column(String)\n    signup_date = Column(DateTime, nullable=False)


class Role(Base):\n\n    __tablename__ = 'role'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    role_name = Column(String, nullable=False)\n    description = Column(String)


class UserRole(Base):\n\n    __tablename__ = 'user_role'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    user_id = Column(Integer, ForeignKey('user.id'))\n    role_id = Column(Integer, ForeignKey('role.id'))


class Project(Base):\n\n    __tablename__ = 'project'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    description = Column(String)\n    start_date = Column(DateTime)


class ProjectAssignment(Base):\n\n    __tablename__ = 'project_assignment'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    device_id = Column(Integer, ForeignKey('device.id'))\n    project_id = Column(Integer, ForeignKey('project.id'))


class Vendor(Base):\n\n    __tablename__ = 'vendor'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    contact_info = Column(String)\n    address = Column(String)


class DeviceVendor(Base):\n\n    __tablename__ = 'device_vendor'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    device_id = Column(Integer, ForeignKey('device.id'))\n    vendor_id = Column(Integer, ForeignKey('vendor.id'))\n    supplied_date = Column(DateTime)\n    delivery_status = Column(String)


class AuditLog(Base):\n\n    __tablename__ = 'audit_log'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    action = Column(String, nullable=False)\n    timestamp = Column(DateTime, nullable=False)\n    user_id = Column(Integer, ForeignKey('user.id'))\n    description = Column(String)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    device_1 = Device(name="Device A", manufacturer_id=1, purchase_date=date(2022, 3, 15), warranty_period=12, price=500)
    device_2 = Device(name="Device B", manufacturer_id=2, purchase_date=date(2023, 5, 21), warranty_period=24, price=1000)
    device_3 = Device(name="Device C", manufacturer_id=1, purchase_date=date(2021, 11, 30), warranty_period=18, price=750)
    device_4 = Device(name="Device D", manufacturer_id=3, purchase_date=date(2020, 1, 5), warranty_period=36, price=1500)
    manufacturer_1 = Manufacturer(name="Manufacturer X", contact_email="contact@manufacturerx.com", phone_number="123-456-7890")
    manufacturer_2 = Manufacturer(name="Manufacturer Y", contact_email="contact@manufacturery.com", phone_number="987-654-3210")
    manufacturer_3 = Manufacturer(name="Manufacturer Z", contact_email="contact@manufacturerz.com", phone_number="456-789-1230")
    manufacturer_4 = Manufacturer(name="Manufacturer W", contact_email="contact@manufacturerw.com", phone_number="321-654-9870")
    component_1 = Component(device_id=1, component_type="CPU", description="Intel i7", serial_number="SN123456")
    component_2 = Component(device_id=2, component_type="GPU", description="NVIDIA GTX 2080", serial_number="SN789101")
    component_3 = Component(device_id=3, component_type="RAM", description="16GB DDR4", serial_number="SN111213")
    component_4 = Component(device_id=4, component_type="SSD", description="Samsung 1TB", serial_number="SN141516")
    maintenance_record_1 = MaintenanceRecord(device_id=1, maintenance_date=date(2023, 8, 5), summary="Annual checkup", cost=100)
    maintenance_record_2 = MaintenanceRecord(device_id=1, maintenance_date=date(2023, 2, 16), summary="Replaced battery", cost=50)
    maintenance_record_3 = MaintenanceRecord(device_id=2, maintenance_date=date(2023, 7, 23), summary="Replaced GPU", cost=300)
    maintenance_record_4 = MaintenanceRecord(device_id=3, maintenance_date=date(2023, 1, 9), summary="Upgraded RAM", cost=150)
    user_1 = User(username="jdoe", email="jdoe@example.com", password_hash="hashed_pwd_1", signup_date=date(2022, 6, 14))
    user_2 = User(username="asmith", email="asmith@example.com", password_hash="hashed_pwd_2", signup_date=date(2023, 7, 20))
    user_3 = User(username="bkumar", email="bkumar@example.com", password_hash="hashed_pwd_3", signup_date=date(2021, 2, 5))
    user_4 = User(username="mlara", email="mlara@example.com", password_hash="hashed_pwd_4", signup_date=date(2020, 12, 24))
    role_1 = Role(role_name="Admin", description="System administrator")
    role_2 = Role(role_name="Manager", description="Operations Manager")
    role_3 = Role(role_name="Technician", description="Field Technician")
    role_4 = Role(role_name="Viewer", description="Data Viewer")
    user_role_1 = UserRole(user_id=1, role_id=1)
    user_role_2 = UserRole(user_id=2, role_id=2)
    user_role_3 = UserRole(user_id=3, role_id=3)
    user_role_4 = UserRole(user_id=4, role_id=4)
    project_1 = Project(name="Project Alpha", description="Initial Phase", start_date=date(2022, 1, 10))
    project_2 = Project(name="Project Bravo", description="Development", start_date=date(2022, 8, 5))
    project_3 = Project(name="Project Charlie", description="Testing", start_date=date(2023, 3, 20))
    project_4 = Project(name="Project Delta", description="Deployment", start_date=date(2023, 11, 1))
    project_assignment_1 = ProjectAssignment(device_id=1, project_id=1)
    project_assignment_2 = ProjectAssignment(device_id=2, project_id=2)
    project_assignment_3 = ProjectAssignment(device_id=3, project_id=3)
    project_assignment_4 = ProjectAssignment(device_id=4, project_id=4)
    vendor_1 = Vendor(name="Vendor X", contact_info="vendorx@example.com", address="123 Main St")
    vendor_2 = Vendor(name="Vendor Y", contact_info="vendory@example.com", address="456 Broadway Ave")
    vendor_3 = Vendor(name="Vendor Z", contact_info="vendorz@example.com", address="789 Elm St")
    vendor_4 = Vendor(name="Vendor W", contact_info="vendorw@example.com", address="321 Spruce Dr")
    device_vendor_1 = DeviceVendor(device_id=1, vendor_id=1, supplied_date=date(2021, 7, 21), delivery_status="Delivered")
    device_vendor_2 = DeviceVendor(device_id=2, vendor_id=2, supplied_date=date(2023, 6, 30), delivery_status="Pending")
    device_vendor_3 = DeviceVendor(device_id=3, vendor_id=3, supplied_date=date(2020, 10, 15), delivery_status="Delivered")
    device_vendor_4 = DeviceVendor(device_id=4, vendor_id=4, supplied_date=date(2022, 2, 12), delivery_status="Back Ordered")
    audit_log_1 = AuditLog(action="Login", timestamp=date(2023, 4, 15), user_id=1, description="User login successful")
    audit_log_2 = AuditLog(action="Update", timestamp=date(2023, 5, 10), user_id=2, description="Updated device details")
    audit_log_3 = AuditLog(action="Delete", timestamp=date(2023, 7, 25), user_id=3, description="Deleted component record")
    audit_log_4 = AuditLog(action="Create", timestamp=date(2023, 8, 11), user_id=4, description="Created new project")
    
    
    
    session.add_all([device_1, device_2, device_3, device_4, manufacturer_1, manufacturer_2, manufacturer_3, manufacturer_4, component_1, component_2, component_3, component_4, maintenance_record_1, maintenance_record_2, maintenance_record_3, maintenance_record_4, user_1, user_2, user_3, user_4, role_1, role_2, role_3, role_4, user_role_1, user_role_2, user_role_3, user_role_4, project_1, project_2, project_3, project_4, project_assignment_1, project_assignment_2, project_assignment_3, project_assignment_4, vendor_1, vendor_2, vendor_3, vendor_4, device_vendor_1, device_vendor_2, device_vendor_3, device_vendor_4, audit_log_1, audit_log_2, audit_log_3, audit_log_4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
