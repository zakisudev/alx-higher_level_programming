#!/usr/bin/python3
""" List all state objects by using sqlalchemy """

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    """ create engine, add city and commit """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    new_session = Session()

    new_state = State(name='California')
    new_city = City(name='San Fransisco', state=new_state)
    new_state.cities.append(new_city)
    new_session.add(new_state)
    new_session.add(new_city)
    new_session.commit()
