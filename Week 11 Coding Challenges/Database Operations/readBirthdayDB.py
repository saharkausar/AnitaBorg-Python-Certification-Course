#   SCRIPT: readBirthdayDB.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: Utilizes a MySQL database to store information about a group of friends' birthday celebration details.
#
#   Note: This file is to be used in tandem with the birthdayDB.sql database file

#Imports the mysql module
import mysql.connector;

#Establishes the connection to the database
conn = mysql.connector.connect(host = 'localhost', database = 'birthdayDB', user = 'root', password = 'TestPass')

#Sets up the cursor connection
cursor_tournament = conn.cursor()

#Selects our desired tournament table information
cursor_tournament.execute("Select * from tourneys")
rows = cursor_tournament.fetchall()

#Prints out the tournament table
print("Tourneys Table: ")
for x in rows:
    print(x)

#Closes the tournament table connection
cursor_tournament.close()

#Sets up the cursor connection
cursor_dinners = conn.cursor()

#Selects our desired dinners table information
cursor_dinners.execute("Select * from dinners")
rows = cursor_dinners.fetchall()

#Prints out the dinners table
print("Dinners Table: ")
for y in rows:
    print(y)

#Closes the dinners table connection
cursor_dinners.close()

#Sets up the cursor connection
cursor_name = conn.cursor()

#Selects our desired information (Names from the dinners table)
cursor_name.execute("SELECT Name FROM dinners")
column = cursor_name.fetchall()

#Prints out the desired information (Names from the dinners table)
print("Retrieving names from dinners table: ")
for z in column:
    print(z)

#Closes the tournament table connection
cursor_name.close()

#Closes the connection to the database
conn.close()
