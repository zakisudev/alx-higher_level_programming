#!/usr/bin/python3
""" Print all states from the database """
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    new_session = Session()

    data = new_session.query(State, City)\
        .join(State, State.id == City.state_id).order_by(City.id)
    for state, city in data.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    new_session.close()
