import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="classicmodels")
if con:
    print("connection created")
else:
    print("not")

cur=con.cursor()
# cur.execute("show tables")
# cur.execute("create table ajith(id int,name varchar(20))")
# x="insert into ajith(id,name) values(%s,%s)"
# y=[(1,"A"),(2,"B")]
# cur.executemany(x,y)
cur.execute("select * from ajith")
# cur.execute("update ajith set name='z'where id=1")
x=cur.fetchall()
print(x)
# con.commit()
con.close()
