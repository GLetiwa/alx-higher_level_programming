#!/usr/bin/python3
"""
Print State object with name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Extract command line arguments
    username, password, database, state_name = sys.argv[1], \
            sys.argv[2], sys.argv[3], sys.argv[4]

    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(username, password, database), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the specified name and display the result
    state = session.query(State).filter_by(name=state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")
