#!/usr/bin/python3
""" fetch all from state table"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if not state:
        print('Nothing')

    else:
        print(f"{state.id}: {state.name}")

    session.close()
