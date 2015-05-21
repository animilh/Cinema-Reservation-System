from settings import spells, cn


class CinemaInterface:

    def __init__(self, movie_manager):
        self.__cinema = movie_manager


    def help_me(self):
        print('You have the following options:')
        for spell in spells:
            print(spell)


    def show_movies(self):
        movies = self.__cinema.show_movies()
        print("Current movies:")
        for movie in movies:
            print('[{}] - {} ({})'.format(movie[0], movie[1], movie[2]))


    def get_movie(self, id_movie):
        movie_name = self.__cinema.get_movie(id_movie)
        print("Projections for movie '{}':".format(movie_name['name']))


    def get_movie_projections(self, id_movie_if):
        projections = self.__cinema.get_movie_projections(id_movie_if)
        for proj in projections:
            print('[{}] - {} {} ({})'.format(proj[0], proj[1], proj[2], proj[3]))


    def get_name_and_raiting(self, id_movie):
        movie_name_and_raiting = self.__cinema.get_name_and_raiting(id_movie)
        for move in movie_name_and_raiting:
            print("{} {} ".format(move[0], move[1]))


    def get_row_and_col(self, username):
        col_and_row = self.__cinema.get_row_col(username)
        return col_and_row


    def choose_seat(self):
        try:
            choice_row = int(input("Step 4 (Seats): Choose seat's row>"))
            choice_col = int(input("Step 4 (Seats): Choose seat's col>"))

            if not cn.is_available(choice_row, choice_col):
                print("This seats are already taken.")
            if not cn.is_in_map(choice_row, choice_col):
                print("You have chosen invalid seats.")

            cn.choose_seat(choice_row, choice_col)
            cn.print_map()

            return (choice_row, choice_col)
        except (ValueError, TypeError):
            print("Bad input for row and col.")


    def give_up(self):
        print("Exit from the reservation portal.")


    def already_reserved(self, id_projection):
        reserved = self.__cinema.already_reserved(id_projection)
        for reser in reserved:
            cn.put_x(reser[0], reser[1])


    def cancel_reservation(self, username):
        cn.cancel_reservation(
            self.get_row_and_col(username)[0], self.get_row_and_col(username)[1])
        self.__cinema.cancel_reservation(username)
        print("The reservation of {} has been canceled.".format(username))


    def insert_reservation(self, username, projection_id, row, col):
        self.__cinema.insert_reservation(username, projection_id, row, col)


    def start(self):
        print('Welcome to Magic Cinema Reservation System')

        while True:
            choice = input('>')
            if str(choice) not in spells:
                print('Bad input. For more information please type help')
                continue

            if str(choice) == 'help':
                self.help_me()
                continue

            if choice == 'show_movies':
                self.show_movies()
                continue

            if choice == 'show_movie_projections':
                id_movie = input('id movie>')
                self.get_movie(id_movie)
                self.get_movie_projections(id_movie)
                continue

            if str(choice) == 'exit':
                print('Exit the Magic System')
                break

            if str(choice) == 'cancel_reservation':
                username = input('name>')
                self.cancel_reservation(username)
                continue

            if str(choice) == 'make_reservation':
                username = input("Step 1 (User): Choose name>")
                if username == "exit":
                    self.give_up()
                    continue

                number_of_tickets = int(input(
                    "Step 1 (User): Choose number of tickets>"))
                if number_of_tickets == "exit":
                    self.give_up()
                    continue

                self.show_movies()
                id_movie_if = input("Step 2 (Movie): Choose a movie>")
                if id_movie_if == "exit":
                    self.give_up()
                    continue

                self.get_movie(id_movie_if)
                self.get_movie_projections(id_movie_if)
                id_projection = input("Step 3 (Projection): Choose a projection>")
                if id_projection == "exit":
                    self.give_up()
                    continue

                projections = self.__cinema.get_movie_projections(id_movie_if)
                id_projections_list = [proj[0] for proj in projections]

                while int(id_projection) not in id_projections_list:
                    print("Doesn't exist such a projection_id.Try again")
                    id_projection = input("Step 3 (Projection): Choose a projection>")
                self.already_reserved(id_projection)
                cn.print_map()


                count = int(number_of_tickets)
                while count > 0:
                    try:
                        result = self.choose_seat()
                        if None not in (result[0], result[1]):
                            self.insert_reservation(
                                username, id_projection, result[0], result[1])
                        count -= 1
                    except TypeError:
                        print("Type valid row and col.")
                      
                         


                print("Your reservation is successful")
                final = str(input("Step 5 (Confirm - type 'finalize')>"))
                if final == 'finalize':
                    print('Thanks!')
                else:
                    print('Type help to see other options.')
                    continue
