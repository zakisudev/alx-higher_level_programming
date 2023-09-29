#!/usr/bin/python3
""" List all states that contain the letter 'a' """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    new_session = Session()

    state = new_session.query(State).filter(State.name == argv[4]).first()
    print(state.id) if (state) else print("Not found")
    new_session.close()
