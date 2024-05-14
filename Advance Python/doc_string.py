# Doc_String
import mysql.connector
my_db = mysql.connector.connect(
    host = "localhost",
    user = "navin",
    passwd = "1234"
)
mycursor = my_db.cursor()
mycursor.execute('show database')

for i in mycursor:
    print(i)





# def ramesh():
#     '''Hello I am ramesh
#     How are you doing! '''
#     print(24)
# ramesh()
# print(ramesh.__doc__)