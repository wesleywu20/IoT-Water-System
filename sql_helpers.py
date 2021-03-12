
import sqlite3
from sqlite3 import Error

database = "water.db"
conn = None




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
        global database
        conn = establish_connection(database)

    return conn

def save_changes():
    conn.commit()
    
def close_db():
    conn.close()


