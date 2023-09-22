#!/usr/bin/python3
"""lists first  object of a certain database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    st_ cities = session.query(State, City).
    filter(State.id == City.state_id).all()

    for state, city in st_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
