
import sqlite3
from project._config import DATABASE

with sqlite3.connect(DATABASE) as connection:

    # get a user object used to execute sql commands
    c = connection.cursor()

    # create the table
    c.execute(""" CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
    status INTEGER NOT NULL)""")

    # insert dummy data into the table
    c.execute('INSERT INTO tasks(name, due_date, priority, status)' 
    'VALUES("Finish this tutorial", "03/25/2013", 10, 1)')

    # insert dummy data into the table
    c.execute('INSERT INTO tasks(name, due_date, priority, status)' 
    'VALUES("Finish Real Python 2 tutorial", "04/24/2014", 10, 1)')