import sqlite3
from movie import Movie
from settings import DB_NAME

connection = sqlite3.connect(DB_NAME)
connection.row_factory = sqlite3.Row

spells = [
    'show_movies',
    'show_movie_projections',
    'make_reservation',
    'cancel_reservation',
    'exit',
    'help'
]

def help_me():
    print('You have the following options:')
    for spell in spells:
        print(spell)

def show_movies():
    movies = Movie.show_movies(connection)
    print("Current movies:")
    for movie in movies:
        print('[{}] - {} ({})'.format(movie[0], movie[1], movie[2]))

def get_movie(id_movie):
    movie_name = Movie.get_movie(connection, id_movie)
    print("Projections for movie '{}':".format(movie_name['name']))

def get_movie_projections(id_movie):
    projections = Movie.get_movie_projections(connection, id_movie)
    for proj in projections:
        print('[{}] - {} {} ({})'.format(proj[0], proj[1], proj[2], proj[3]))

def cancel_reservation(name):
    Movie.cancel_reservation(connection, name)
    #unmark the seats from the kinosalon
    print("The reservation of {} has been canceled.".format(name))

def start():
    print('Welcome to Magic Cinema Reservation System')

    while True:
        choice = input('>')
        if str(choice) not in spells:
            print('Bad input. For more information please type help')
            continue

        if str(choice) == 'help':
            help_me()
            continue

        if choice == 'show_movies':
            show_movies()
            continue

        if choice == 'show_movie_projections':
            id_movie = input('id movie>')
            get_movie(id_movie)
            get_movie_projections(id_movie)
            continue

        if str(choice) == 'exit':
            print('Exit the Magic System')
            break

        if str(choice) == 'cancel_reservation':
            name = input('name>')
            cancel_reservation(name)
            continue

        if str(choice) == 'make_reservation':
            username = input("Step 1 (User): Choose name>")
            number_of_tickets = input("Step 1 (User): Choose number of tickets>")
            show_movies()
            id_movie = input("Step 2 (Movie): Choose a movie>")
            get_movie(id_movie)
            get_movie_projections(id_movie)
            id_projection = input("Step 3 (Projection): Choose a projection>")
            #print a map of cinema
            #Step 4 (Seats): Choose seat 1>
            #Step 4 (Seats): Choose seat 2>
            #print the reservation
            #insert the reservation in table reservations!!!
            final = input("Step 5 (Confirm - type 'finalize')>")
            if final == 'finalize':
                print('Thanks!')
            else:
                print('Type help to see other options.')
            continue

def main():
    start()

if __name__ == '__main__':
    main()
