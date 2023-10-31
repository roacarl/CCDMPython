

import mysql.connector

#create connection
conn = mysql.connector.connect(host = "localhost",user = "root",passwd = "ceit")

#create cursor object
mycursor = conn.cursor()

#mycursor.execute('Create Database liklikbuklibrary')
mycursor.execute('use liklikbuklibrary')

#create table
tablebooks = """create table Books (BookID int primary key, Title vacrchar(20),Author varchar(20),Gener varchar(20))"""

#mycursor.execute(tablebooks)

# insert value into table
insertvalue1 = """insert into Books value(101,"Days of the Week","Jow Blue","Education")"""

mycursor.execute(insertvalue1)

#create second variable
insertvalue2 = """insert into value(102,"My ABCs","Jane Brown","Education")"""
mycursor.execute(insertvalue2)

#Viewing the Data
mycursor.execute('select * from Books')
result = mycursor.fetchall()
conn.commit()

for row in result:
    print(row)
    print("\n")
