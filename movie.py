class Movie:

    SHOW_MOVIES = """
        SELECT id, name, rating
        FROM movies
        ORDER BY id
    """

    GET_MOVIE = """
        SELECT name
        FROM movies
        WHERE id = ?
    """
<<<<<<< HEAD

=======
    GET_MOVIE_AND_RAITING = """
        SELECT name,rating
        FROM movies
        WHERE id = ?
"""
>>>>>>> ani
    SHOW_MOVIE_PROJECTIONS = """
        SELECT id, date, time, type
        FROM projections
        WHERE movie_id = ?
    """

    CANCEL_RESERVATION = """
        DELETE FROM reservations
        WHERE username = ?
    """
<<<<<<< HEAD


    @classmethod
    def show_movies(cls, connection):
        cursor = connection.cursor()
        result = cursor.execute(cls.SHOW_MOVIES)
        return result.fetchall()

    @classmethod
    def get_movie(cls, connection, movie_id):
        cursor = connection.cursor()
        movie_name = cursor.execute(cls.GET_MOVIE, (movie_id, ))
        return movie_name.fetchone()

    @classmethod
    def get_movie_projections(cls, connection, movie_id):
        cursor = connection.cursor()
        result = cursor.execute(cls.SHOW_MOVIE_PROJECTIONS, (movie_id, ))
=======
    GET_ROW_AND_COL = """
    SELECT row, col
    FROM reservations
    WHERE username = ?
    """

    INSERT_RESERVATION = """
    INSERT INTO reservations(username,projection_id,row,col)
    VALUES (?,?,?,?)
 """

    GET_ALREADY_RESERVED = """
    SELECT row,col
    FROM reservations
    WHERE projection_id=?
    """

    def __init__(self, conn):
        self.__conn = conn

    def show_movies(self):
        cursor = self.__conn.cursor()
        result = cursor.execute(Movie.SHOW_MOVIES)
        return result.fetchall()

    def get_movie(self, movie_id):
        cursor = self.__conn.cursor()
        movie_name = cursor.execute(Movie.GET_MOVIE, (movie_id, ))
        return movie_name.fetchone()


    def get_movie_projections(self, movie_id):
        cursor = self.__conn.cursor()
        result = cursor.execute(Movie.SHOW_MOVIE_PROJECTIONS, (movie_id, ))
        return result.fetchall()


    def cancel_reservation(self, username):
        cursor = self.__conn.cursor()
        cursor.execute(Movie.CANCEL_RESERVATION, (username, ))
        self.__conn.commit()


    def get_row_col(self, username):
        cursor = self.__conn.cursor()
        result_e = cursor.execute(Movie.GET_ROW_AND_COL, (username, ))
        return result_e.fetchone()


    def get_name_and_raiting(self, movie_id):
        cursor = self.__conn.cursor()
        result_one = cursor.execute(Movie.GET_MOVIE_AND_RAITING, (movie_id, ))
        return result_one.fetchone()


    def insert_reservation(self, username, projection_id, row, col):
        cursor = self.__conn.cursor()
        cursor.execute(
            Movie.INSERT_RESERVATION, (username, projection_id, row, col))
        self.__conn.commit()


    def already_reserved(self, projection_id):
        cursor = self.__conn.cursor()
        result = cursor.execute(Movie.GET_ALREADY_RESERVED, (projection_id, ))
>>>>>>> ani
        return result.fetchall()

    @classmethod
    def cancel_reservation(cls, connection, name):
        cursor = connection.cursor()
        cursor.execute(cls.CANCEL_RESERVATION, (name, ))
        connection.commit()

