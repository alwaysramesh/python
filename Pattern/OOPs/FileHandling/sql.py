import mysql.connector as conn

mydb = conn.connect(host="localhost",user="root", password="1234", database="krishn")

myc = mydb.cursor()

mysql = "select * from emp"

myc.execute(mysql)
res = myc.fetchall()

for i in res:
    print("SN",i[0], end="  ")
    print("Name",i[1], end="  ")
    print("Deparment",i[2], end="  ")
    print("Salary",i[3], end="  ")
    print()