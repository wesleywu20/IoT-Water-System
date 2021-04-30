
import sqlite3
import pandas as pd
import datetime as dt
from sqlite3 import Error

database_name = "water.db"
conn = None

RANGE_QUERY = "SELECT timestamp, flow FROM water_flow WHERE timestamp BETWEEN '{}' AND '{}'"
INSERT_QUERY = "INSERT INTO water_flow (timestamp, flow) VALUES ('{}', '{}')"

GET_AVG_QUERY = "SELECT value FROM meta WHERE name = 'avg'"
GET_LAST_UPDATED_QUERY = "SELECT value from meta WHERE name = 'last_updated'"
GET_TOTAL_QUERY = "SELECT value from meta WHERE name = 'total'"
GET_HIST_INDEX_QUERY = "SELECT value from meta WHERE name = 'hist{}'"
GET_MAX_QUERY = "SELECT value from meta WHERE name = 'max'"

SET_AVG_QUERY = "UPDATE meta SET value='{}' WHERE name = 'avg'"
SET_LAST_UPDATED_QUERY = "UPDATE meta SET value='{}' WHERE name = 'last_updated'"
SET_TOTAL_QUERY = "UPDATE meta SET value='{}' WHERE name = 'total'"
SET_HIST_INDEX_QUERY = "UPDATE meta SET value='{}' WHERE name = 'hist{}'"
SET_MAX_QUERY = "UPDATE meta SET value='{}' WHERE name = 'max'"


# ---------------------------------------------------------------------------------------
# HELPER

def dt_to_string(time):
	return dt.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')


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
	print(flow)
	print(timestamp)
	query(db, INSERT_QUERY.format(flow, timestamp))
	save_changes()
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
	
	times = list(df['timestamp'])
	datetimes = []
	for time in times:
		datetimes.append(dt_to_string(time))
	
	return (datetimes, list(df['flow']))


# returns tuple of (old_avg, last_updated) of types (double, datetime)
def get_old_avg():
	db = access_db()
	return (query(db, GET_AVG_QUERY)[0][0], dt_to_string(query(db, GET_LAST_UPDATED_QUERY)[0][0]))


# sets the old average stored in the database
def set_old_avg(avg, dt):
	db = access_db()
	query(db, SET_AVG_QUERY.format(avg))
	query(db, SET_LAST_UPDATED_QUERY.format(dt))



# returns tuple of (total, last_updated) of types (double, datetime)
def get_total():
	db = access_db()
	return (query(db, GET_TOTAL_QUERY)[0][0], dt_to_string(query(db, GET_LAST_UPDATED_QUERY)[0][0]))


# sets the old total stored in the database
def set_total(total, dt):
	db = access_db()
	query(db, SET_TOTAL_QUERY.format(total))
	query(db, SET_LAST_UPDATED_QUERY.format(dt))


# returns tuple of (max, last_updated) of types (double, datetime)
def get_total():
	db = access_db()
	return (query(db, GET_MAX_QUERY)[0][0], dt_to_string(query(db, GET_LAST_UPDATED_QUERY)[0][0]))


# sets the max stored in the database
def set_total(maximum, dt):
	db = access_db()
	query(db, SET_MAX_QUERY.format(maximum))
	query(db, SET_LAST_UPDATED_QUERY.format(dt))



# returns tuple of (hist value, last_updated) of types (double, datetime)
def get_hist_index(index):
	db = access_db()
	print(GET_HIST_INDEX_QUERY.format(index))
	return query(db, GET_HIST_INDEX_QUERY.format(index))[0][0]


# sets the histogram value at an index stored in the database
def set_hist_index(index, val):
	db = access_db()
	query(db, SET_HIST_INDEX_QUERY.format(val, index))


def get_hist():
	hist = []
	for i in range(24):
		hist.append(get_hist_index(i))
	return hist


def set_hist(hist):
	if(len(hist) != 24):
		print("histogram has inappropriate length")
	for i in range(24):
		set_hist_index(i, hist[i])




