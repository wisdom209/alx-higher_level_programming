#!/usr/bin/python3
"""Creates a city table"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from model_state import Base, State

Base = declarative_base()

class City(Base):
    """class representing city table"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement='auto',
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

