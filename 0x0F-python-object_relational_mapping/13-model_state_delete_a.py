#!/usr/bin/python3
""" Add 'Louisiana' to the state in databse """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    new_session = session()

    states = new_session.query(State).filter(State.name.like('%a%'))
    for state in states.all():
        new_session.delete(state)

    new_session.commit()
    new_session.close()
