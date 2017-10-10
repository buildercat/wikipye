import sqlite3

sqlite_file = 'D:\Noah\Documents\SQlite3Databases\database.db'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
data = ['']
link = ''
tableName = 'table'
new_field = 'Counts'
new_field2 = 'Path'
fieldType = 'INTEGER'
fieldType2 = 'TEXT'
new_field3 = 'Start'
fieldType3 = 'TEXT'
x = 0
f = open('database', "r")


def setUp():
    sqlite_file = 'D:\Noah\Documents\SQlite3Databases\database.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    x = 0


def createTable(table_name, new_field3, new_field2, new_field, fieldType3, fieldType2, fieldType, c):
    c.execute("DROP TABLE IF EXISTS t")
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
              .format(tn=table_name, nf=new_field3, ft=fieldType3))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
              .format(tn=table_name, cn=new_field, ct=fieldType))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
              .format(tn=table_name, cn=new_field2, ct=fieldType2))
    c.execute("ALTER TABLE t ADD COLUMN 'Loop' TEXT")
    print('createTable')


def openFile():
    global f
    data = f.readlines()
    for link in range(len(data)):
        data[link] = data[link][:-2]
        print('openFile')
    print(data)
    return data


def insertData(tableName, new_field3, new_field2, new_field, x, data):
    x=-1
    pig = 'test'
    print(data)
    for link in data:

        print(link)
        link = link.split(',')
        v,b,n,m = link
        b = int(b)
        x = x + 1
        c.execute("INSERT OR IGNORE INTO t VALUES (?, ?, ?, ?)", (v, b, n, m))
        print('insertData')


def close():
    global f
    f.close()
    conn.commit()
    conn.close()
    print('close')
