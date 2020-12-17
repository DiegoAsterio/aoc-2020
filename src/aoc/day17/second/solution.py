from collections import defaultdict

from aoc.utils import local_path, get_lines

import pdb

def easy_board():
    return defaultdict(easy_board)

class FourDBoard:
    def __init__(self, configuration):
        z = 0
        w = 0
        self.board = easy_board()
        for x, row in enumerate(configuration):
            for y, elem in enumerate(row):
                if elem == '#':
                    self.board[x][y][z][w] = True
        self.generation = 0

    def neighbourhood(self, x1, y1, z1, w1, with_center=True):
        for x in range(x1-1, x1+2):
            for y in range(y1-1, y1+2):
                for z in range(z1-1, z1+2):
                    for w in range(w1-1, w1+2):
                        if x != x1 or y != y1 or z != z1 or w != w1 or with_center:
                            yield x, y, z, w
                        
    def active_neighbours(self, x1, y1, z1, w1):
        counter = 0
        for x2, y2, z2, w2 in self.neighbourhood(x1, y1, z1, w1, with_center=False):
            if x2 in self.board:
                if y2 in self.board[x2]:
                    if z2 in self.board[x2][y2]:
                        if w2 in self.board[x2][y2][z2]:
                            counter += 1
        return counter
        
    def becomes_active(self, x, y, z, w):
        active = self.active_neighbours(x, y, z, w)
        if x in self.board:
            if y in self.board[x]:
                if z in self.board[x][y]:
                    if w in self.board[x][y][z]:
                        return active == 2 or active == 3
        return active == 3
            
    def populate_around(self, x1, y1, z1, w1, new_configuration):
        for x2, y2, z2, w2 in self.neighbourhood(x1, y1, z1, w1):
            if self.becomes_active(x2, y2, z2, w2):
                new_configuration[x2][y2][z2][w2] = True
                    
    def next_turn(self):
        new_configuration = easy_board()
        for x in self.board:
            for y in self.board[x]:
                for z in self.board[x][y]:
                    for w in self.board[x][y][z]:
                        self.populate_around(x, y, z, w, new_configuration)
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
                    for w in self.board[x][y][z]:
                        counter += 1
        return counter

    def execute_cycle(self):
        self.til_generation(6)
        
def count_living_cells(configuration):
    board = FourDBoard(configuration)
    board.execute_cycle()
    return board.count_alive()

def main():
    to_input = "../input"
    path = local_path(__file__, to_input)

    config = get_lines(path)

    print(count_living_cells(config))

if __name__ == "__main__":
    main()
                         

