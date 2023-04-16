#!/usr/bin/python3
""" fetch all from state table"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)

    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")
        session.close()
