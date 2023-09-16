#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

Base = declarative_case()


class State(Base):
    """ Implements the class State """
    __table_name__ = 'states'
    id = Column(Integer, nullable=True, unique=True,
            Primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
