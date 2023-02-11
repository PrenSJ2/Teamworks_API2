from sqlalchemy import Column, DATETIME, Integer, Float, String, Boolean, Text, ForeignKey



class User(BaseModel):
    UID: int
    DateofBirth: str
    First_name: str
    Last_name: str
    Email: str
    Password: str
    Phone_number: str
    isHost: bool

class Office(BaseModel):
    OID: int
    Name: str
    Location: str
    NumGuests: str
    Sqft: str
    Description: str
    Hourly: float
    MinHours: str
    Amenities: str
    Features: str
    Image: str
    UID: int

class Booking(BaseModel):
    BID: int
    Start_datetime: str
    End_datetime: str
    isActive: bool
    Total_hours: float
    NumGuests: int
    Activity: str
    TimePeriod: str
    OID: int
    HID: int
    OName: str
    OLocation: str
    UID: int
    GName: str
    OfficePrice: float
    ServiceFee: float
    FinalPrice: float

class Addon(BaseModel):
    AID: int
    Name: str
    Quantity: int
    Price: float
    ImgName: str
    OID: int