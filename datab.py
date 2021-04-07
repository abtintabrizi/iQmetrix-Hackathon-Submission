import sqlite3
from main import Employee

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE employees (
            name text,
            city text,
            job text
            )""")

def insertEmp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:name, :city, :job)", {'name': emp.name, 'city': emp.city, 'job': emp.job})

def getEmpsByCity(city):
    c.execute("SELECT * FROM employees WHERE city=:city", {'city': city})
    return c.fetchall()

def getEmpsByJob(job):
    c.execute("SELECT * FROM employees WHERE job=:job", {'job': job})
    return c.fetchall()

conn.close()