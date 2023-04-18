#!/usr/bin/python
"""Script that list all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv
"""import module"""


if __name__ = "__main__":
	db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
	cur = db.cursor()
	cur.execute("SELECT cities.id, cities.name, states.name\
			FROM cities\
			JOIN states ON cities.states_id = states.id\
			ORDER BY cities.id ASC")

	for row in cursor.fetchall():
			print(row)

			cur.close()
			db.close()
