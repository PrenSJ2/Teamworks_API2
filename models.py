from typing import List
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    UID = Column(Integer, primary_key=True)
    DateofBirth = Column(DateTime)
    First_name = Column(String)
    Last_name = Column(String)
    Email = Column(String, unique=True)
    Password = Column(String)
    Phone_number = Column(String)
    isHost = Column(Boolean)

class Office(Base):
    __tablename__ = 'offices'
    OID = Column(Integer, primary_key=True)
    Name = Column(String)
    Location = Column(String)
    NumGuests = Column(String)
    Sqft = Column(String)
    Description = Column(String)
    Hourly = Column(Float)
    MinHours = Column(String)
    Amenities = Column(String)
    Features = Column(String)
    Image = Column(String)
    UID = Column(Integer)

class Booking(Base):
    __tablename__ = 'bookings'
    BID = Column(Integer, primary_key=True)
    Start_datetime = Column(DateTime)
    End_datetime = Column(DateTime)
    isActive = Column(Boolean)
    Total_hours = Column(Float)
    NumGuests = Column(Integer)
    Activity = Column(String)
    TimePeriod = Column(String)
    OID = Column(Integer)
    HID = Column(Integer)
    OName = Column(String)
    OLocation = Column(String)
    UID = Column(Integer)
    GName = Column(String)
    OfficePrice = Column(Float)
    ServiceFee = Column(Float)
    FinalPrice = Column(Float)

class Addon(Base):
    __tablename__ = 'addons'
    AID = Column(Integer, primary_key=True)
    Name = Column(String, unique=True)
    Quantity = Column(Integer)
    Price = Column(Float)
    ImgName = Column(String)
    OID = Column(Integer)

engine = create_engine('sqlite:///data.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
