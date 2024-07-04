import mysql.connector
mydb=mysql.connector.connect(host="Localhost",username="root",password="nandini2123",database="mydb")
mycurs=mydb.cursor()
#mycurs.execute("create database mydb")
#mycurs.execute("show databases")
#mycurs.execute("create table users(name varchar(50), email varchar(50), password varchar(50))")
#mycurs.execute("show tables")
#mysql="Insert into users(name,email,password)values(%s,%s,%s)"
#val=("nandini","umanandini98@gmail.com","nandin")
#mycurs.execute(mysql,val)
mycurs.execute("select * from users")
#for i in mycurs:
 #   print(i)