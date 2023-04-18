#!/usr/bin/python3
"""
Start link class to table in database
"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""import modules from sys and sqlalchemy"""

Base = declarative_base()


class State(Base):
	"""State Class"""
	__tablename__ = 'states'

	id = column(Integer, primary_key=True, autoincreament=True, nullable=False)
	name = Column(String(128), nullable=False)
