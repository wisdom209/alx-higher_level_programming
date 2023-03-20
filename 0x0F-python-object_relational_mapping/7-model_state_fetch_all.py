#!/usr/bin/python3
"""Fetches all the states"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State

if __name__ == '__main__':
	db_username = sys.argv[1]
	db_pass = sys.argv[2]
	db_name = sys.argv[3]
	host = "localhost"
	port = 3306
	engine = engine = create_engine(
		f"mysql://{db_username}:{db_pass}@{host}:{port}/{db_name}")

	Session = sessionmaker(bind=engine)
	session = Session()
	states = session.query(State).order_by(State.id).all()
	for state in states:
		print(f"{state.id}: {state.name}")  # getting table data
