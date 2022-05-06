# import mysql.connector
import sqlite3
# con=mysql.connector.connect(host='localhost',user='root',password='root123',database='king')
con=sqlite3.connect('students.db')
print(con)
cur=con.cursor()
# cur.execute("CREATE TABLE data1 (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), phone BIGINT(255),sl VARCHAR(255),sl2 VARCHAR(255),sch VARCHAR(255),sch2 VARCHAR(255),ss VARCHAR(255),ss2 VARCHAR(255),st VARCHAR(255),st2 VARCHAR(255),sn VARCHAR(255),sn2 VARCHAR(255),sw VARCHAR(255),sw2 VARCHAR(255),shirt VARCHAR(255),coat VARCHAR(255),pl VARCHAR(255),pl2 VARCHAR(255),pw VARCHAR(255),pw2 VARCHAR(255),ph VARCHAR(255),ph2 VARCHAR(255),pm VARCHAR(255),pm2 VARCHAR(255),pg VARCHAR(255),pg2 VARCHAR(255),other VARCHAR(255),kurta VARCHAR(255),pant VARCHAR(255),date VARCHAR(255), deliverydate VARCHAR(255), image LONGBLOB NOT NULL)")
cur.execute("CREATE TABLE studentdata (id  INTEGER PRIMARY KEY AUTOINCREMENT ,fistname VARCHAR(255),lastname VARCHAR(255),fathername VARCHAR(255),email VARCHAR(255), contactnumber BIGINT(255),gender VARCHAR(255),address VARCHAR(255),city VARCHAR(255),state VARCHAR(255),collagename VARCHAR(255),course VARCHAR(255),year VARCHAR(255),listcourses VARCHAR(255),reference VARCHAR(255))")
con.commit()
print("done")
# """
#
# ,coat VARCHAR(255),pl VARCHAR(255),pl2 VARCHAR(255),pw VARCHAR(255),pw2 VARCHAR(255),ph VARCHAR(255),ph2 VARCHAR(255),pm VARCHAR(255),pm2 VARCHAR(255),pg VARCHAR(255),pg2 VARCHAR(255),kurta VARCHAR(255),pant VARCHAR(255),other VARCHAR(255),date VARCHAR(255), deliverydate VARCHAR(255))
#
#
# """