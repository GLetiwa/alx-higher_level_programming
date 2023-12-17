#!/usr/bin/python3
"""
State objects that contain letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects containing the letter 'a' and display the results
    states_with_a = session.query(State).filter(State.name.ilike('%a%'))\
            .order_by(State.id).all()
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))
