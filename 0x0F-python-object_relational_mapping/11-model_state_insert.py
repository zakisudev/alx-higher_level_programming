#!/usr/bin/python3
""" Add 'Louisiana' to the state in databse """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    new_session = session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
