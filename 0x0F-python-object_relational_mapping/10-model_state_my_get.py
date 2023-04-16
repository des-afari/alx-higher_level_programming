#!/usr/bin/python3
"""State from database by name
"""

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

    if "'" not in sys.argv[4]:
        check = session.query(State).filter_by(name=sys.argv[4]).scalar()
        if check is None:
            print("Not found")
        else:
            query = session.query(State).filter_by(name=sys.argv[4])
            for row in query.all():
                print(f"{row.id}")

    session.close()
