#import pymssql
import pyodbc

mydb = pyodbc.connect(driver="ODBC Driver 17 for SQL Server",host="(localdb)\MSSQLLocalDB",user="Sameer",password='1234',database="test_DB")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM EMPLOYEES")

#result1=mycursor.fetchone()
result=mycursor.fetchall()

#for i in result1:
 #   print(i)

with open('myfile.txt','w') as f:
    for r in result:
        line=','.join(str(x) for x in r)
        f.write(line+'\n')

mydb.close()
