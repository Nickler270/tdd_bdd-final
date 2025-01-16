#service/models.py
from enum import Enum
from sqlalchemy import Column, Integer, String, Float, Boolean, Enum as SqlEnum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    """Model for the Product table"""
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63), nullable=False)
    category = db.Column(db.String(63), nullable=False)
    available = db.Column(db.Boolean, default=True)
    description = db.Column(db.String(256))


class Category(Enum):
    UNKNOWN = "Unknown"
    CLOTHS = "Cloths"
    FOOD = "Food"
    HOUSEWARES = "Housewares"
    AUTOMOTIVE = "Automotive"
    TOOLS = "Tools"