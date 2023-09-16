#!/usr/bin/python3
""" List all city objects by using sqlalchemy relationship """

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy import create_engine
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    new_session = Session()

    for city in new_session.query(City).order_by(City.id):
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
