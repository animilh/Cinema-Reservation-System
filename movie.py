class Movie:

    SHOW_MOVIE = """
        SELECT id, name, raiting
        FROM movies
        ORDER BY id
    """

    SHOW_MOVIE_PROJECTIONS = """
        SELECT id, date, time, type
        FROM projections
        WHERE id = ?
    """


    @classmethod
    def get_movies(cls, connection):
        cursor = connection.cursor()
        result = cursor.execute(cls.SHOW_MOVIE)
        return result.fetchall()

    @classmethod
    def get_movie_projections(cls, connection, id_projection):
        cursor = connection.cursor()
        result = cursor.execute(cls.SHOW_MOVIE_PROJECTIONS)
        return result.fetchall()


