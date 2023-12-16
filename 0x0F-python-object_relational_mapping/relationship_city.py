#!/usr/bin/python3
"""
A Python file similar to model_state.py named model_city.py
that contains the class definition of a City.
"""

from relationship_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    City Class

    Attributes:
        id (int)
        name (str)
        state_id (int)
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
