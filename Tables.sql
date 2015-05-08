DROP TABLE IF EXISTS movies,projections,reservations;

CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY, name TEXT, raiting FLOAT )
);

INSERT INTO movies(name , raiting)
    VALUES ("The Godfather",9.8),
    ("Firm",6.7),
    ("Limitless",8.9),
    ("Apocalypto",7.5);

CREATE TABLE IF NOT EXISTS projections(id PRIMARY KEY
    ,movie_id INTEGER ,
     type TEXT,
      date DATE,
       time TIME,
       FOREIGN KEY (movie_id) REFERENCES movies(id)
       );

INSERT INTO projections(type,date,time)
    VALUES ("2D","2014-04-01","19:10"),
    ("3DX","2015-01-02","22:30"),
    ("3D","2013-07-12","13:12"),
    ("2D","2015-03-21","10:10"),
    ("3DX","2015-07-11","20:00"),
     ("4D","2015-08-28","21:45:00");

CREATE TABLE IF NOT EXISTS reservations (id INTEGER PRIMARY KEY,
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


