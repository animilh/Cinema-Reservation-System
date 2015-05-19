DROP TABLE IF EXISTS movies;

CREATE TABLE movies(
    id INTEGER PRIMARY KEY, name TEXT, rating FLOAT
);

INSERT INTO movies(name, rating)
    VALUES ("The Godfather",9.8),
    ("Firm",6.7),
    ("Limitless",8.9),
    ("Apocalypto",7.5);

DROP TABLE IF EXISTS projections;

CREATE TABLE projections(id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    type TEXT,
    date DATE,
    time TIME,
    FOREIGN KEY (movie_id) REFERENCES movies(id));

INSERT INTO projections(movie_id,type,date,time)
    VALUES (1,"2D","2014-04-01","19:10"),
    (2,"3DX","2015-01-02","22:30"),
    (3,"3D","2013-07-12","13:12"),
    (4,"2D","2015-03-21","10:10"),
    (2,"3DX","2015-07-11","20:00"),
     (3,"4D","2015-08-28","21:45:00");

DROP TABLE IF EXISTS reservations;

CREATE TABLE reservations (id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    projection_id INTEGER,
    row INTEGER,
    col INTEGER,
    FOREIGN KEY (projection_id) REFERENCES projections(id)
    );

INSERT INTO reservations(username,projection_id,row,col)
    VALUES
    ("Deyan Denchev",3,5,5),
    ("Peter Tanev",2,2,6),
    ("Ivan Ivanov",1,7,9),
    ("Lili Mihailova",4,4,7)
    ;
