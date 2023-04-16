#!/usr/bin/python3
"""Delete all states that coontain 'a'"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

if __name__ == "__main__":
    """ Engine connection
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """ Session handling
    """

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like('%a%'))\
                        .delete(synchronize_session=False)

    session.commit()
    session.close()
