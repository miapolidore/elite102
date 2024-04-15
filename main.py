import mysql.connector # type: ignore

cnx = mysql.connector.connect(user="rohan", password="pass1234", host="localhost")
print(cnx)

'''
connection = mysql.connector.connect(user = ' ', database = ' ', password = ' ')
cursor = connection.cursor()
testQuery = ("SELECT * FROM "put something here idk")
cursor.execute(testQuery)

for item in cursor:
    print(item)

cursor.close()
connection.close()
'''
