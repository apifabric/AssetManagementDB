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


class User(Base):\n    '''description: This table stores user information.'''\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    username = Column(String, nullable=False)\n    email = Column(String, nullable=False)\n    joined_date = Column(DateTime, nullable=False)\n    profile_photo_id = Column(Integer, ForeignKey('photos.id'))


class Photo(Base):\n    '''description: This table stores photo data associated with users.'''\n    __tablename__ = 'photos'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    url = Column(String, nullable=False)\n    created_at = Column(DateTime, nullable=False)\n    description = Column(String)


class Product(Base):\n    '''description: This table keeps track of the product details.'''\n    __tablename__ = 'products'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    price = Column(DECIMAL, nullable=False)\n    stock_quantity = Column(Integer, nullable=False)\n    creation_date = Column(DateTime, nullable=False)


class Order(Base):\n    '''description: This table records user orders.'''\n    __tablename__ = 'orders'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)\n    order_date = Column(DateTime, nullable=False)\n    total_amount = Column(DECIMAL, nullable=False)\n    status = Column(String, nullable=False)


class LineItem(Base):\n    '''description: This table represents each line item within an order.'''\n    __tablename__ = 'line_items'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)\n    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)\n    quantity = Column(Integer, nullable=False)\n    price = Column(DECIMAL, nullable=False)


class Category(Base):\n    '''description: This table defines product categories.'''\n    __tablename__ = 'categories'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    description = Column(String)\n    created_at = Column(DateTime, nullable=False)


class ProductCategory(Base):\n    '''description: Associative table linking products and categories.'''\n    __tablename__ = 'product_categories'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)\n    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)


class Inventory(Base):\n    '''description: Represents inventory containing multiple products.'''\n    __tablename__ = 'inventory'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    location = Column(String, nullable=False)\n    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)\n    quantity = Column(Integer, nullable=False)


class Cart(Base):\n    '''description: A shopping cart entity for tracking users' selected items.'''\n    __tablename__ = 'carts'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)\n    created_at = Column(DateTime, nullable=False)


class CartItem(Base):\n    '''description: Each product added to a user's cart.'''\n    __tablename__ = 'cart_items'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)\n    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)\n    quantity = Column(Integer, nullable=False)


class Review(Base):\n    '''description: Stores reviews users give to products.'''\n    __tablename__ = 'reviews'\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)\n    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)\n    rating = Column(Integer, nullable=False)\n    comment = Column(String)\n    review_date = Column(DateTime, nullable=False)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    user1 = User(username="john_doe", email="john@example.com", joined_date=date(2021, 1, 15))
    photo1 = Photo(url="https://example.com/image1.jpg", created_at=date(2021, 1, 10), description="Profile Photo")
    product1 = Product(name="Widget", price=30.00, stock_quantity=100, creation_date=date(2021, 1, 5))
    order1 = Order(user_id=1, order_date=date(2021, 1, 20), total_amount=60.00, status="Shipped")
    line_item1 = LineItem(order_id=1, product_id=1, quantity=2, price=30.00)
    category1 = Category(name="Gadgets", created_at=date(2021, 1, 3))
    product_category1 = ProductCategory(product_id=1, category_id=1)
    inventory1 = Inventory(location="Warehouse A", product_id=1, quantity=50)
    cart1 = Cart(user_id=1, created_at=date(2021, 1, 25))
    cart_item1 = CartItem(cart_id=1, product_id=1, quantity=1)
    review1 = Review(product_id=1, user_id=1, rating=5, comment="Excellent product!", review_date=date(2021, 1, 27))
    
    
    
    session.add_all([user1, photo1, product1, order1, line_item1, category1, product_category1, inventory1, cart1, cart_item1, review1])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
