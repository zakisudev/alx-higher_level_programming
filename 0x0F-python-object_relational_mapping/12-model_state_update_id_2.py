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

    new_state = new_session.query(State).filter(State.id == 2).first()
    new_state.name = "New Mexico"
    new_session.commit()
    new_session.close()
