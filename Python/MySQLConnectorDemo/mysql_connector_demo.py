import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="employee_db"
)

c = db.cursor()

c.execute("DELETE FROM employee WHERE empid=1")
db.commit()
c = db.cursor()
c.execute("select * from employee")

employee_data = c.fetchall()

for e in employee_data:
    print(e)

db.close()