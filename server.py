import sqlite3
con=sqlite3.connect("mydatabase.db")
cur=con.cursor()
#cur.execute("create table if not exists students(name varchar(20),email varchar(20),password varchar(20))")
#cur.execute('insert into students values("nandini","1233","A")')
#cur.execute('insert into students values("MERCY","1234","B")')
#cur.execute('insert into students values("DIMPU","1235","C")')
#cur.execute('delete from students where name="mercy" ')
cur.execute('update students set name="nandini" where email="1235"')

x=cur.execute('select *from students')
print(x.fetchall())
#x=cur.execute("show tables")

con.commit()
print(x)