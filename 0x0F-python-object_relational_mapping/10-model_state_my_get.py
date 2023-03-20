#!/usr/bin/python3
"""Fetches state having given name"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    Access to the database and get the state having a
    given name from the database.
    """
    db_username = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    host = "localhost"
    port = 3306
    engine = create_engine(
        f"mysql://{db_username}:{db_pass}@{host}:{port}/{db_name}")
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(
        State.name == state_name).order_by(State.id)
    if (states.count() == 0):
        print("Not found")
    for state in states:
        print(f"{state.id}")
