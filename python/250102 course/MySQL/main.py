import  mysql.connector

mysql = mysql.connector.connect(
    host="eric9",
    user="root",
    password="5czRLDzw",
)

mycursor = mysql.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)