#!/usr/bin/python3
""" List all states that contain the letter 'a' """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    states = session().query(State).filter(state.name == argv[4])
    if (states.count() == 0):
        print("Not found")
    else:
        for state in states:
        print("{}: {}".format(state.id, ))
    session().close()