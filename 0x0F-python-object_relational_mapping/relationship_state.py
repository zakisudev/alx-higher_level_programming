#!/usr/bin/python3
""" Improved state class for db """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ Implements the class State """
    __tablename__ = 'states'
    id = Column(Integer, nullable=True, unique=True,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
