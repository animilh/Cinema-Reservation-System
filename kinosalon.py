class Map:

    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != ""]
        self.map = [list(line) for line in lines]
        self.seats_availability = {}
        for i in range(1, 11):
            for j in range(2, 21):
                if self.map[i][j] == "X":
                    self.seats_availability[(i, j)] = 1
                elif self.map[i][j] == ".":
                    self.seats_availability[(i, j)] = 0

    def print_map(self):
        for x in self.map:
            s = "".join(x)
            print(s)

    def is_available(self, row, col):
        if self.seats_availability[row, col * 2] == 1:
            return False
        return True

    def is_in_map(self, row, col):
        if row in range(1, 11) and col in range(1, 11):
            return True
        return False

    def choose_seat(self, row, col):
        if row > 10 or col > 10:
            return False
        self.seats_availability[(row, col * 2)] = 1
        self.map[row][col * 2] = "X"
        return True

    def count_available_seats(self):
        count = 0
        for row in range(1, 11):
            for col in range(2, 21):
                if self.map[row][col] == ".":
                    count += 1
        return count

    def cancel_reservation(self, row, col):
        self.seats_availability[(row, col * 2)] = 0
        self.map[row][col * 2] = "."
        return True

    def put_x(self,row,col):
        self.seats_availability[(row, col * 2)] = 1
        self.map[row][col * 2] = "X"
        return True
