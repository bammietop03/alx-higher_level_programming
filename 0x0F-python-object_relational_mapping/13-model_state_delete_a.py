#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).filter(State.name.contains('a'))
    
    if data is not None:
        for info in date:
            session.delete(state)

    session.commit()

    session.close()
