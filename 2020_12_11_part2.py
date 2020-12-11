import numpy as np
from enum import Enum

class CellType(Enum):
    LIBRE = 'L'
    OCCUP = '#'
    FLOOR = '.'
    def __repr__(self):
        return self.value

def diagonal_without_elem(ma, i, j):
    pivot = min(i, j)
    diag = ma.diagonal(j - i)
    return np.append(diag[:pivot], diag[pivot + 1:])
    
class Neighbourhood:
    def __init__(self, seats, row, col):
        n, m = seats.shape
        self.neighbours = []
        l = col - 1
        found = False
        while l >= 0 and not found:
            if seats[row, l] != CellType.FLOOR:
                found = True
                self.neighbours.append(seats[row, l])
            l -= 1                        # <-
        r = col + 1
        found = False
        while r < m and not found:
            if seats[row, r] != CellType.FLOOR:
                found = True
                self.neighbours.append(seats[row, r])
            r += 1                        # ->
        u = row - 1
        found = False
        while u >= 0 and not found:
            if seats[u, col] != CellType.FLOOR:
                found = True
                self.neighbours.append(seats[u, col])
            u -= 1                        # ^
        d = row + 1
        found = False
        while d < n and not found:
            if seats[d, col] != CellType.FLOOR:
                found = True
                self.neighbours.append(seats[d, col])
            d += 1                        # v
        l = col - 1
        u = row - 1
        found = False
        while l >= 0 and u >= 0 and not found:
            if seats[u, l] != CellType.FLOOR:
                found = True
                self.neighbours.append(seats[u, l])
            l -= 1                        # <-
            u -= 1                        # ^
        r = col + 1
        u = row - 1
        found = False
        while r < m and u >= 0 and not found:
            if seats[u, r] != CellType.FLOOR:
                found = True
                self.neighbours.append(seats[u, r])
            r += 1                        # ->
            u -= 1                        # ^
        r = col + 1
        d = row + 1
        found = False
        while r < m and d < n and not found:
            if seats[d, r] != CellType.FLOOR:
                found = True
                self.neighbours.append(seats[d, r])
            r += 1                        # ->
            d += 1                        # v
        l = col - 1
        d = row + 1
        found = False
        while l >= 0 and d < n and not found:
            if seats[d, l] != CellType.FLOOR:
                found = True
                self.neighbours.append(seats[d, l])
            l -= 1                        # <-
            d += 1                        # v
    def occupied(self):
        occupied_seats = [n for n in self.neighbours if n == CellType.OCCUP]
        return len(occupied_seats)

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
        while 0 < pos_row and pos_row < m and 0 < pos_col and pos_col < m:
            yield seats[pos_row, pos_col]

    def count_occupied(self, seats, row, col):
        counter = 0
        for drow, dcol in self.directions:
            for cell in self.neighbours_in_direction(seats, row, col, drow, dcol):
                if cell == CellType.Occupied:
                    counter += 1
                    break
        return counter
                           
class Seats:
    def __init__(self, conf0):
        self.seats = np.array([ [CellType(x) for x in row] for row in conf0])
        self.stable = False

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

    def new_celltype(self,cell, i, j):
        neighbourhood = Neighbourhood(self.seats,i,j)
        if cell == CellType.LIBRE:
            if neighbourhood.occupied() == 0:
                return CellType.OCCUP
        elif cell == CellType.OCCUP:
            if neighbourhood.occupied() >= 5:
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
