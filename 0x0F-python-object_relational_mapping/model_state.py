#!/usr/bin/python3
"""Creates a state table"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """class representing state table"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement='auto',
                primary_key=True)
    name = Column(String(128), nullable=False)
