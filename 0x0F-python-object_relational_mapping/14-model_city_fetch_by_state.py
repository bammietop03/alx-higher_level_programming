#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa:
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(City, State).join(State)\
        .filter(State.id == City.state_id).order_by(City.id).all()

    for city, state in data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
