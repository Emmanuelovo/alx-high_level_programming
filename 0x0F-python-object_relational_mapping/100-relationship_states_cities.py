#!/usr/bin/python3
"""
creates thte python STate "California" with the city "San Francisco"
from the database hbtn_0e_100_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import Ciity
import sys

if __name__ == '__main__':
	"""Connection arguments"""
	user = sys.argv[1]
	password = sys.argv[2]
	dbname = sys.argv[3]

	"""start the engine"""
	engine = create_engine('myssql+mysqldb://{}:{}@localhost:3306/{}'.format(user, password, dbname), pool_pre_ping=True)

	"""create all tables stored in this metadata"""
	Base.metadata.create_all(engine)

	"""create a configured session Class"""
	Session = sessionmaker(bind=engine)

	"""create session instance"""
	session = Session()

	newState = State(name='California')
	newCity = City(name='San Francisco')
	newState.cities.append(newCity)

	session.add(newState)
	session.add(newCity)
	session.commit()

