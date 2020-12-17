from collections import defaultdict

from aoc.utils import local_path, get_lines

def easy_board():
    return defaultdict(easy_board)

class Board:
    def __init__(self, configuration):
        z = 0
        self.board = easy_board()
        for x, row in enumerate(configuration):
            for y, elem in enumerate(row):
                if elem == '#':
                    self.board[x][y][z] = True
        self.generation = 0

    def neighbourhood(self, x1, y1, z1, with_center=True):
        for x in range(x1-1, x1+2):
            for y in range(y1-1, y1+2):
                for z in range(z1-1, z1+2):
                    if x != x1 or y != y1 or z != z1 or with_center:
                        yield x, y, z
                        
    def active_neighbours(self, x1, y1, z1):
        counter = 0
        for x2, y2, z2 in self.neighbourhood(x1, y1, z1, with_center=False):
            if x2 in self.board:
                if y2 in self.board[x2]:
                    if z2 in self.board[x2][y2]:
                        counter += 1
        return counter
        
    def becomes_active(self, x, y, z):
        active = self.active_neighbours(x, y, z)
        if x in self.board:
            if y in self.board[x]:
                if z in self.board[x][y]:
                    return active == 2 or active == 3
        return active == 3
            
    def populate_around(self, x1, y1, z1, new_configuration):
        for x2, y2, z2 in self.neighbourhood(x1, y1, z1):
            if self.becomes_active(x2, y2, z2):
                new_configuration[x2][y2][z2] = True
                    
    def next_turn(self):
        new_configuration = easy_board()
        for x in self.board:
            for y in self.board[x]:
                for z in self.board[x][y]:
                    self.populate_around(x, y, z, new_configuration)
        self.board = new_configuration
        self.generation += 1

    def til_generation(self, n):
        while self.generation < n:
            self.next_turn()

    def count_alive(self):
        counter = 0
        for x in self.board:
            for y in self.board[x]:
                for z in self.board[x][y]:
                    counter += 1
        return counter

    def execute_cycle(self):
        self.til_generation(6)
        
def count_living_cells(configuration):
    board = Board(configuration)
    board.execute_cycle()
    return board.count_alive()

def main():
    to_input = "../input"
    path = local_path(__file__, to_input)

    config = get_lines(path)

    print(count_living_cells(config))

if __name__ == "__main__":
    main()
                         

