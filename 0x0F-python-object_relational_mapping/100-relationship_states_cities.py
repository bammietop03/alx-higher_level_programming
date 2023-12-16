#!/usr/bin/python3
"""
A script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cali = State(name="California")
    san_f = City(name="San Francisco")

    cali.cities.append(san_f)

    session.add(cali)
    session.commit()

    session.close()
