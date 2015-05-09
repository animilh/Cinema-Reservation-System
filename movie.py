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

    SHOW_MOVIE_PROJECTIONS = """
        SELECT id, date, time, type
        FROM projections
        WHERE movie_id = ?
    """

    CANCEL_RESERVATION = """
        DELETE FROM reservations
        WHERE username = ?
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
    def cancel_reservation(cls, connection, name):
        cursor = connection.cursor()
        cursor.execute(cls.CANCEL_RESERVATION, (name, ))
        connection.commit()

