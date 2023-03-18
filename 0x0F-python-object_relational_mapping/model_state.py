#!/usr/bin/python3
"""Creates a state table"""
import sys
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base = declarative_base()

    class State(Base):
        """class representing state table"""
        __tablename__ = 'states'
        id = Column(Integer, autoincrement='auto',
                    primary_key=True, nullable=False, unique=True)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
