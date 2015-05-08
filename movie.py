class Movie:

    SHOW_MOVIE = """
        SELECT id, name, raiting
        FROM movies
        ORDER BY id
    """

    SHOW_MOVIE_PROJECTIONS = """
        SELECT id, date, time, type
        FROM projections
        WHERE movie_id = ?
    """


    @classmethod
    def get_movies(cls, connection):
        cursor = connection.cursor()
        result = cursor.execute(cls.SHOW_MOVIE)
        return result.fetchall()

    @classmethod
    def get_movie_projections(cls, connection, movie_id):
        cursor = connection.cursor()
        result = cursor.execute(cls.SHOW_MOVIE_PROJECTIONS, (movie_id, ))
        return result.fetchall()