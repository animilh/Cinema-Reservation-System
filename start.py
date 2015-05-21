import sqlite3
from settings import DB_NAME
from magic_reservation_system import CinemaInterface
from movie import Movie


def main():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    movie_manager = Movie(conn)
    interface = CinemaInterface(movie_manager)
    interface.start()

if __name__ == "__main__":
    main()
