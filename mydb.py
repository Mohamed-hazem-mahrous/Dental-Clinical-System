import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'habiba'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE honmono_db")

# cursorObject.execute("CREATE table users(First_Name varchar(20) not null,Last_Name varchar(20) not null,Sex varchar(20) not null,Email varchar(50) not null unique,Mobile varchar(14) not null,Birth DATE,Password varchar(50) not null,Start_Time TIME,End_Time TIME,type varchar(20) not null);")

print("all done")