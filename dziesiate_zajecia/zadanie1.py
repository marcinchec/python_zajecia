#stworz tabele przechowujaca dane o ksiazkach. Przetestuj podstawowe operacje na bazie

import sqlite3

connection = sqlite3.connect("example.db")
cursor=connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS
test(id integer, name text, title text)''')
cursor.execute('''INSERT INTO test VALUES (1, 'Mickiewicz', 'Pan Tadeusz')''')
cursor.execute('''INSERT INTO test VALUES (2, 'Prus', 'Lalka')''')
cursor.execute('''DELETE FROM test WHERE id=2''')
cursor.execute('''UPDATE test SET title='Dziady' WHERE id=1''')
#cursor.execute('''DELETE FROM test''')
#connection.commit()

for row in cursor.execute('SELECT * FROM test'):
    print row

connection.close()