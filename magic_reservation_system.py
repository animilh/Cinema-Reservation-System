import sqlite3
from movie import Movie

connection = sqlite3.connect('cinema.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

spells = [
    'show_movies',
    'show_movie_projections',
    'make_reservation',
    'cancel_reservation',
    'exit',
    'help'
]


print('Welcome to Magic Cinema Reservation System')

while True:
    choice = input('>')
    if str(choice) not in spells:
        print('Bad input. For more information please type help')
        continue
    break


if choice == 'help':
    print('You have the following options:')
    for spell in spells:
        print(spell)

if choice == 'show_movies':
    movies = Movie.get_movies(connection)
    print("Current movies:")
    for movie in movies:
        print('[{}] - {} ({})'.format(movie[0], movie[1], movie[2]))

if choice == 'show_movie_projections':
    id_movie = input('id movie>')
    projections = Movie.get_movie_projections(connection, id_movie)
    for proj in projections:
        print('[{}] - {} {} ({})'.format(proj[0], proj[1], proj[2], proj[3]))

# if choice == 'make_reservation':
#     Movie.make_reservation()

# if choice == 'cancel_reservation':
#     Movie.cancel_reservation()

if choice == 'exit':
    print('Press ^D to exit the Magic System')
