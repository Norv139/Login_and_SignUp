from os import curdir
import sqlite3
from sqlite3.dbapi2 import Cursor
import hash
import time

bd = sqlite3.connect('./date_base.db')

cursor = bd.cursor()

def sql_reqest(username, password, method="GET"):

    password = hash.hash_fn(password)

    if method=="GET":

        cursor.execute(('SELECT * FROM Users WHERE Name = "'+username+'" AND Password = "'+password+'"'))

        result = cursor.fetchall()

        if result == []:
            return("Error user not find")
        else:
            return [result[0][1],result[0][2]]

    elif method=="POST":

        cursor.execute(('SELECT * FROM Users WHERE Name = "'+username+'"'))
        result_serch = cursor.fetchall()

        if result_serch == []:

            cursor.execute('SAVEPOINT "RESTOREPOINT"')

            cursor.execute(('INSERT INTO Users (Name, Password) VALUES ("'+username+'", "'+password+'")'))

            cursor.execute('RELEASE "RESTOREPOINT";')

            return "You have successfully registered"

        else:
            
            return "Error user is find"