
import sqlite3
import pandas as pd
from sqlite3 import Error

database_name = "water.db"
conn = None

RANGE_QUERY = "SELECT timestamp, flow FROM water_flow WHERE timestamp BETWEEN '{}' AND '{}'"
INSERT_QUERY = "INSERT INTO water_flow VALUES ('{}', '{}')"

# ---------------------------------------------------------------------------------------
# DATABASE ACCESS

def establish_connection(file):
	try:
		conn = sqlite3.connect(file)
		return conn
	except Error as e:
		print(e)

	return None


def query(connection, command):
	cursor = connection.cursor()
	cursor.execute(command)
	results = cursor.fetchall()
	cursor.close()
	return results


def access_db():
	global conn
	if conn is None:
		global database_name
		conn = establish_connection(database_name)

	return conn


def save_changes():
	global conn
	conn.commit()


def close_db():
	global conn
	conn.close()


# ---------------------------------------------------------------------------------------
# SPECIFIC QUERY FUNCTIONS


def insert_flow(flow, timestamp):
	db = access_db()
	query(db, INSERT_QUERY.format(flow, timestamp))
	return

# NOTE: These functions assume that time_start and time_end both follow this format:
#			YYYY-MM-DD HH:MM:SS

# returns a list of tuples in the format (timestamp, flow)
def get_range_tuple_list(time_start, time_end):
	db = access_db()
	results = query(db, RANGE_QUERY.format(time_start, time_end))
	return results


# returns a dataframe with columns: timestamp, flow
def get_range_into_dataframe(time_start, time_end):
	db = access_db()
	dataframe = pd.read_sql_query(RANGE_QUERY.format(time_start, time_end), db)
	return dataframe


# returns a tuple with two elements being a list of timestamps and a list of flows
def get_range(time_start, time_end):
	df = get_range_into_dataframe(time_start, time_end)
	return (list(df['timestamp']), list(df['flow']))

