#service/models.py
from enum import Enum
from sqlalchemy import Column, Integer, String, Float, Boolean, Enum as SQLAEnum

class Category(Enum):
    UNKNOWN = "Unknown"
    CLOTHS = "Cloths"
    FOOD = "Food"
    HOUSEWARES = "Housewares"
    AUTOMOTIVE = "Automotive"
    TOOLS = "Tools"

class Product(db.Model):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    description = Column(String(256))
    price = Column(Float)
    available = Column(Boolean)
    category = Column(SQLAEnum(Category))
