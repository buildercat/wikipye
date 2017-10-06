import sqlite3

sqlite_file = 'D:\Noah\Documents\SQlite3Databases\database.db'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
data = ['']
link = ''
tableName = 'table'
new_field = 'Start'
new_field2 = 'Jumps'
fieldType = 'TEXT'
fieldType2 = 'INTEGER'
new_field3 = 'id'
fieldType3 = 'INTEGER'
x = 0
f = None

def setUp():
    sqlite_file = 'D:\Noah\Documents\SQlite3Databases\database.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    x = 0

def createTable():

    global tableName
    global new_field3
    global new_field2
    global new_field
    global fieldType3
    global fieldType2
    global fieldType
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
              .format(tn=tableName, nf=new_field3, ft=fieldType3))
    c.execute('ALTER TABLE {tn} ({nf} {ft} )'\
              .format(tn=tableName, nf=new_field, ft=fieldType))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
              .format(tn=tableName, cn=new_field2, ct=fieldType2))
    print('createTable')
def openFile():
    global data
    global link
    global f
    f = open('database', "r")
    data = f.readlines()
    for link in range(len(data)):
        data[link] = data[link][:-2]
        print('openFile')

def insertData():
    global tableName
    global new_field3
    global new_field2
    global new_field
    global link
    global x
    for link in data:
        x = x + 1
        c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (x, link)".\
            format(tn=tableName, idf=new_field3, cn=new_field))
        print('insertData')

def close():
    global f
    f.close()
    conn.commit()
    conn.close()
    print('close')
