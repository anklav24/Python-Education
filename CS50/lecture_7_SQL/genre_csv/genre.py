import csv
import sqlite3

con = sqlite3.connect('genre_db.sqlite')  # Create db if doesn't exist.
cur = con.cursor()

cur.execute("DROP table IF EXISTS shows")
cur.execute("DROP table IF EXISTS genres")
cur.execute("DROP table IF EXISTS shows_genres")

cur.execute("CREATE TABLE shows (id INTEGER, title TEXT, PRIMARY KEY(id));")
cur.execute("CREATE TABLE genres (id INTEGER, name TEXT, PRIMARY KEY(id));")

cur.execute("""
            CREATE TABLE shows_genres (
            show_id INTEGER,
            genre_id INTEGER,
            FOREIGN KEY(show_id) REFERENCES shows(id),
            FOREIGN KEY(genre_id) REFERENCES genres(id));
            """)

with open("Favorite TV Shows.csv", "r") as file:
    reader = csv.DictReader(file)
    genre_set = set()
    for row in reader:
        title_row = row["title"].strip().lower()

        cur.execute("INSERT INTO shows (title) VALUES (?)", (title_row,))
        show_last_id = cur.lastrowid

        for genre_row in row["genres"].lower().split(", "):
            cur.execute("INSERT INTO shows_genres (show_id, genre_id) VALUES (?, ?)", (show_last_id, show_last_id))
            genre_set.add(genre_row)

    for genre in genre_set:
        cur.execute("INSERT INTO genres (name) VALUES (?)", (genre,))

    con.commit()
