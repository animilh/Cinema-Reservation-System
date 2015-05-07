import sqlite3


connection = sqlite3.connect("cinema.db")
cursor = connection.cursor()

create_movies = """
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY, name TEXT, raiting FLOAT )
"""
cursor.execute(create_movies)

cursor.execute("""INSERT INTO movies(name , raiting)
    VALUES ("The Godfather",9.8),
    ("Firm",6.7),
    ("Limitless",8.9),
    ("Apocalypto",7.5)
""")

create_projections = """
CREATE TABLE IF NOT EXISTS projections(id PRIMARY KEY
    ,movie_id INTEGER ,
     type TEXT,
      date DATE,
       time TIME,
       FOREIGN KEY (movie_id) REFERENCES movies(id)
       )
"""
cursor.execute(create_projections)
cursor.execute("""INSERT INTO projections(type,date,time)
    VALUES ("2D","2014-04-01","19:10"),
    ("3DX","2015-01-02","22:30"),
    ("3D","2013-07-12","13:12"),
    ("2D","2015-03-21","10:10"),
    ("3DX","2015-07-11","20:00")
""")

create_reservations = """
CREATE TABLE IF NOT EXISTS reservations (id INTEGER PRIMARY KEY,
    username TEXT,
    projection_id INTEGER,
    row INTEGER,
    col INTEGER,
    FOREIGN KEY (projection_id) REFERENCES projections(id)
    )
"""
cursor.execute(create_reservations)
cursor.execute("""INSERT INTO reservations(username,row,col)
    VALUES
    ("Deyan Denchev",5,5),
    ("Peter Tanev",2,6),
    ("Ivan Ivanov",7,9),
    ("Lili Mihailova",4,7)
""")

connection.commit()
