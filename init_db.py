import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Выход на один', 'Демонстрация элемента в моем исполнении https://youtu.be/KQMEFD_471A')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Выход на два', 'Демонстрация элемента в моем исполнении https://youtu.be/9C1js6IjpVc')
            )

connection.commit()
connection.close()
