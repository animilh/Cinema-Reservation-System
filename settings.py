from kinosalon import Map

DB_NAME = "cinema.db"
SQL_FILE = "Tables.sql"

spells = [
    'show_movies',
    'show_movie_projections',
    'make_reservation',
    'cancel_reservation',
    'exit',
    'help'
]

cn = Map("kinosalon.txt")
