import sqlite3
from deyan_movie import Movie
from settings import DB_NAME
from kinosalon import Map

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

cn = Map("kinosalon.txt")


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


def get_movie_projections(id_movie_if):
    projections = Movie.get_movie_projections(connection, id_movie_if)
    for proj in projections:
        print('[{}] - {} {} ({})'.format(proj[0], proj[1], proj[2], proj[3]))


def get_name_and_raiting(id_movie):
    movie_name_and_raiting = Movie.get_name_and_raiting(connection, id_movie)
    print(
        "{} {} ".format(movie_name_and_raiting[0], movie_name_and_raiting[1]))


def get_row_and_col(username):
    col_and_row = Movie.get_row_col(connection, username)
    return col_and_row


def choose_seat():
    choice_row = int(input("Step 4 (Seats): Choose seat's row>"))
    choice_col = int(input("Step 4 (Seats): Choose seat's col>"))
    if not cn.is_in_map(choice_row, choice_col):
        print("You have chosen invalid seats.")
        return
    if not cn.is_available(choice_row, choice_col):
        print("This seats are already taken")
        return

    cn.choose_seat(choice_row, choice_col)
    cn.print_map()
    return (choice_row, choice_col)


def give_up():
    print("Exit from the reservation portal")


def already_reserved(id_projection):
    reserved = Movie.already_reserved(connection, id_projection)
    for reser in reserved:
        cn.put_x(reser[0], reser[1])


def cancel_reservation(username):
    cn.cancel_reservation(
        get_row_and_col(username)[0], get_row_and_col(username)[1])
    Movie.cancel_reservation(connection, username)
    print("The reservation of {} has been canceled.".format(username))


def insert_reservation(username, projection_id, row, col):
    Movie.insert_reservation(connection, username, projection_id, row, col)
    print("Your reservation is successful")


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
            username = input('name>')
            cancel_reservation(username)
            continue

        if str(choice) == 'make_reservation':
            print(
                "If you want to quit the reservation portal during any of the registration steps type 'exit'")
            username = input("Step 1 (User): Choose name>")
            if username == "Exit":
                give_up()
                continue

            number_of_tickets = int(input(
                "Step 1 (User): Choose number of tickets>"))
            if number_of_tickets == "Exit":
                give_up()
                continue

            show_movies()
            id_movie_if = input("Step 2 (Movie): Choose a movie>")
            if id_movie_if == "Exit":
                give_up()
                continue
            get_movie(id_movie_if)
            get_movie_projections(id_movie_if)
            id_projection_if = input(
                "Step 3 (Projection): Choose a projection>")
            if id_projection_if == "Exit":
                give_up()
                continue

            projections = Movie.get_movie_projections(connection, id_movie_if)
            id_projections_list = [proj[0] for proj in projections]

            while int(id_projection_if) not in id_projections_list:
                print("Doesn't exist such a projection_id.Try again")
                id_projection = input(
                    "Step 3 (Projection): Choose a projection>")
            already_reserved(id_projection_if)
            cn.print_map()

            for count in range(1, number_of_tickets - 1):
                choose_seat()
            #     result = []
            #     result.append(choose_seat())
            # print("Seats:")
            # print(result)

            insert_reservation(
                username, id_projection_if, choose_seat()[0], choose_seat()[1])

            # print("Your resevation:")
            # print("Movie:")
            # get_name_and_raiting(id_projection_if)
            # print("Projection")
            # get_movie_projections(id_projection_if)

            final = str(input("Step 5 (Confirm - type 'finalize')>"))
            if final == 'finalize':
                print('Thanks!')
            else:
                print('Type help to see other options.')
                continue


def main():
    start()

if __name__ == '__main__':
    main()
