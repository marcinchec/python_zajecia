#stworz relacyjny model bazy danych biblioteki. Wprowadz do niej przykladowe dane

import sqlite3

connection = sqlite3.connect("biblioteka.db")
cursor=connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS czytelnik(
    id integer PRIMARY KEY,
    name text, 
    surname text)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ksiazka(
    id integer PRIMARY KEY,
    nr integer, 
    title text,
    id_czyt integer,
    FOREIGN KEY(id_czyt) REFERENCES czytelnik(id))''')

cursor.execute('''INSERT INTO czytelnik VALUES (1, 'Jan', 'Kowalski')''')
cursor.execute('''INSERT INTO czytelnik VALUES (2, 'Andrzej', 'Nowak')''')

cursor.execute('''INSERT INTO ksiazka VALUES (1, 100, 'Tadeusz')''')
cursor.execute('''INSERT INTO ksiazka VALUES (2, 101, 'Lalka')''')

connection.close()