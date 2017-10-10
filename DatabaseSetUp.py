import sqlite3
import SQLibrary as z

sqlite_file = 'D:\Noah\Documents\SQlite3Databases\database.db'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

link = ''
table_name = 't'
new_field = 'Start'
new_field2 = 'Jumps'
fieldType = 'TEXT'
fieldType2 = 'INTEGER'
new_field3 = 'id'
fieldType3 = 'INTEGER'
x = 0

z.createTable(table_name, new_field3, new_field2, new_field, fieldType3, fieldType2, fieldType, c)
data = z.openFile()
z.insertData(table_name, new_field3, new_field2, new_field, x, data)
z.close()
