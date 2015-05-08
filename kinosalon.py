class Map:

    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != ""]
        self.map = [list(line) for line in lines]

    def print_map(self):
        for x in self.map:
            s = "".join(x)
            print(s)

a = Map("kinosalon.txt")
a.print_map()
