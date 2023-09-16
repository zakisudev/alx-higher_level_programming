#!/usr/bin/python3
""" Link class to table in db """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(mind=engine)
    for state in session().query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session().close()
