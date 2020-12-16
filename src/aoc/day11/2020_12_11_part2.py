import numpy as np
from enum import Enum

class CellType(Enum):
    LIBRE = 'L'
    OCCUP = '#'
    FLOOR = '.'

class SeatMap:
    def __init__(self):
        self.directions = [(0, -1),       # <-
                           (-1, -1),      # '\
                           (-1, 0),       # ^ 
                           (-1, +1),      # /'
                           (0, +1),       # ->
                           (+1, +1),      # \,
                           (+1, 0),       # v
                           (+1, -1)]      # ,/

    def neighbours_in_direction(self, seats, row, col, drow, dcol):
        n, m = seats.shape
        pos_row = row + drow
        pos_col = col + dcol
        still_floor = True
        while 0 <= pos_row and pos_row < n and 0 <= pos_col and pos_col < m and still_floor:
            yield seats[pos_row, pos_col]
            still_floor = seats[pos_row, pos_col] == CellType.FLOOR
            pos_row += drow
            pos_col += dcol

    def count_occupied(self, seats, row, col):
        counter = 0
        for drow, dcol in self.directions:
            for cell in self.neighbours_in_direction(seats, row, col, drow, dcol):
                if cell == CellType.OCCUP:
                    counter += 1
        return counter
                           
class Seats:
    def __init__(self, conf0):
        self.seats = np.array([ [CellType(x) for x in row] for row in conf0])
        self.stable = False
        self.seat_map = SeatMap()

    def is_stable(self):
        return self.stable

    def rearrange(self):
        self.stable = True
        new_conf = np.array([ [None for x in row] for row in self.seats ])
        for i, row in enumerate(self.seats):
            for j, cell in enumerate(row):
                new_celltype = self.new_celltype(cell, i, j)
                new_conf[i,j] = new_celltype
                if self.seats[i,j] !=  new_celltype:
                    self.stable = False
        self.seats = new_conf

    def new_celltype(self, cell, i, j):
        occupied = self.seat_map.count_occupied(self.seats, i, j)
        if cell == CellType.LIBRE:
            if occupied == 0:
                return CellType.OCCUP
        elif cell == CellType.OCCUP:
            if occupied >= 5:
                return CellType.LIBRE
        return cell

    def get_occupied_seats(self):
        selection = self.seats.flatten() == CellType('#')
        return len(self.seats.flatten()[selection])
                    
def load_seats(path):
    with open(path) as f:
        lines = f.read().strip().split('\n')
    return Seats(lines)

if __name__ == "__main__":
    path = "2020_12_11.input"
    seats = load_seats(path)

    while not seats.is_stable():
        seats.rearrange()
    occupied = seats.get_occupied_seats()
    print("The number of seats occupied with the final configuration is: {}".format(occupied))
