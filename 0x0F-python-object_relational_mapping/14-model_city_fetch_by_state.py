#!/usr/bin/python3
"""13. Delete states
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    r = session.query(City, State).join(State).order_by(City.id)
    for ins in r.all():
        print(ins[1].name, ": (", ins[0].id, ') ', ins[0].name, sep="")
