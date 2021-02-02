from tkinter import *
import database_operations as db

query = "select * from Cliente"
query2 = "insert into Cliente values('Silas')"

print(db.dql(query))
db.dml(query2)
