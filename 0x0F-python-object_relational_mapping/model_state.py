#!/usr/bin/python3
"""6. First state model"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    __tablename__ = "statesl"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
