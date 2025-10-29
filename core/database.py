#core/database.py

import sqlite3 #import to create and interact with the database 
import os

#Global variables for database path
BASEDIR = os.path.dirname(os.path.abspath(__file__)) #get the current directory of this file, /path/to/loginSystem/core
DBPATH = os.path.join(BASEDIR, '..', 'data','users.db') #create the full path to the database file using our loginSystems file structure, /path/to/loginSystem/data/user.db

#Creates the database and users table if it does not already exist
def createDB():
    os.makedirs(os.path.dirname(DBPATH), exist_ok = True) #create data directory if it doesnt exist
    conn = sqlite3.connect((DBPATH)) #create or connect DB 
    c = conn.cursor() #create cursor, this enables us to execute SLQ commands
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        ) 
    ''') #creates users DB if it does not already exist, if so it does nothing
    conn.commit() #saves changes
    conn.close()

#Checks if username already exists in DB, returns True if so, False if not
def usernameExists(username):
    conn = sqlite3.connect(DBPATH) #connect to DB (/BASEDIR/data/users.db)
    c = conn.cursor() #create cursor, this enables us to execute SLQ commands
    c.execute('''SELECT username FROM users WHERE username = ?''', (username,)) #search for username in DB
    result = c.fetchone() #if username exisit, fetchone() wil return it, if not it will return None
    conn.close()
    if result is None:
        return False #username does not exist in the DB
    else:
        return True #username exists in the DB

#Adds a new user to the database 
def addUser(username, password):
    os.makedirs(os.path.dirname(DBPATH), exist_ok = True)
    conn = sqlite3.connect(DBPATH) #connect to DB (/BASEDIR/data/users.db)
    c = conn.cursor() #create cursor, this enables us to execute SLQ commands

    try:
        c.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password)) #insert new user into DB
        conn.commit()
        print(f"Account created for {username}!")
        return True
    except sqlite3.IntegrityError:
        print("Error: Account creation unsuccessful.")
        return False
    finally:
        conn.close()

#Retrieves the hashed password for a given username from the DB
def gethashWord(username):
    conn = sqlite3.connect(DBPATH) #connect to DB (/BASEDIR/data/users.db)
    c = conn.cursor()
    c.execute('''SELECT password FROM users WHERE username = ?''', (username,))
    result = c.fetchone() 
    conn.close()

    if result is None:
        return None
    else:
        return result[0]

