#!/usr/bin/python3
"""Fetches first state"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    Access to the database and get the first state
    from the database.
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
    state = session.query(State).order_by(State.id).first()
    if (state):
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
