# from sqlalchemy import Column, Integer, String, ForeignKey, Text, Enum, DateTime, func
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# import enum

# Base = declarative_base()

# # Enum for stock status
# class StockStatus(enum.Enum):
#     available = "available"
#     damaged = "damaged"
#     out_of_stock = "out_of_stock"

# # User table
# class User(Base):
#     __tablename__ = 'users'
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     role = Column(String, nullable=False)  # Admin or Manager
    
#     transactions = relationship('Transaction', back_populates='user')

# # Item table
# class Item(Base):
#     __tablename__ = 'items'
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     category = Column(String, nullable=False)

#     stock = relationship('Stock', back_populates='item')

# # Stock table
# class Stock(Base):
#     __tablename__ = 'stock'
    
#     id = Column(Integer, primary_key=True)
#     item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
#     quantity = Column(Integer, nullable=False)
#     status = Column(Enum(StockStatus), default=StockStatus.available)
#     # notes = Column(Text)
    
#     item = relationship('Item', back_populates='stock')
#     transactions = relationship('Transaction', back_populates='stock')

# # Transaction table
# class Transaction(Base):
#     __tablename__ = 'transactions'
    
#     id = Column(Integer, primary_key=True)
#     stock_id = Column(Integer, ForeignKey('stock.id'), nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     action = Column(String, nullable=False)  # e.g., 'add', 'remove'
#     timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
#     stock = relationship('Stock', back_populates='transactions')
#     user = relationship('User', back_populates='transactions')


from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

# Enum for stock status
class StockStatus(enum.Enum):
    available = "available"
    damaged = "damaged"
    out_of_stock = "out_of_stock"

# User table
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)  # Admin or Manager
    
    transactions = relationship('Transaction', back_populates='user')

# Item table
class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)

    stock = relationship('Stock', back_populates='item')

# Stock table
class Stock(Base):
    __tablename__ = 'stock'
    
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(Enum(StockStatus), default=StockStatus.available)
    
    item = relationship('Item', back_populates='stock')
    transactions = relationship('Transaction', back_populates='stock')

# Transaction table
class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String, nullable=False)  # e.g., 'add', 'remove'
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    stock = relationship('Stock', back_populates='transactions')
    user = relationship('User', back_populates='transactions')
