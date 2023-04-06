#overview
# install mysql on compter
# https://dev.mysql.com/downloads/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
 host = 'localhost',
 user = 'root',
 passwd = '1234'

)

#prepare a cursor object

cursorObject = dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE CRMDB")

print("All done")