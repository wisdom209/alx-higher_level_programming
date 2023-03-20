#!/usr/bin/python3
"""join state and city and print the new table"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    """
    Access to the database and print
    state.id (city.id) city.name
    to the database.
    """
    db_username = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306
    engine = create_engine(
        f"mysql://{db_username}:{db_pass}@{host}:{port}/{db_name}")
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")
