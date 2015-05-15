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
    GET_MOVIE_AND_RAITING = """
        SELECT name,rating
        FROM movies
        WHERE id = ?
   """
    SHOW_MOVIE_PROJECTIONS = """
        SELECT id, date, time, type
        FROM projections
        WHERE movie_id = ?
    """

    CANCEL_RESERVATION = """
        DELETE FROM reservations
        WHERE username = ?
    """

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
        return result.fetchall()

    @classmethod
    def cancel_reservation(cls, connection, username):
        cursor = connection.cursor()
        cursor.execute(cls.CANCEL_RESERVATION, (username, ))
        connection.commit()

    @classmethod
    def get_row_col(cls, connection, username):
        cursor = connection.cursor()
        result_e = cursor.execute(cls.GET_ROW_AND_COL, (username, ))
        return result_e.fetchone()

    @classmethod
    def get_name_and_raiting(cls, connection, movie_id):
        cursor = connection.cursor()
        result_one = cursor.execute(cls.GET_MOVIE_AND_RAITING, (movie_id, ))
        return result_one.fetchone()

    @classmethod
    def insert_reservation(cls, connection, username, projection_id, row, col):
        cursor = connection.cursor()
        cursor.execute(
            cls.INSERT_RESERVATION, (username, projection_id, row, col))
        connection.commit()

    @classmethod
    def already_reserved(cls, connection, projection_id):
        cursor = connection.cursor()
        result = cursor.execute(cls.GET_ALREADY_RESERVED, (projection_id, ))
        return result.fetchall()
