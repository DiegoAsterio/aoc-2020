import numpy as np
from enum import Enum

class CellType(Enum):
    LIBRE = 'L'
    OCCUP = '#'
    FLOOR = '.'

class Neighbourhood:
    def __init__(self, seats, row, col):
        self.neighbours = []
        n, m = seats.shape
        up = max(0,row-1)
        down = min(n, row+2)
        l = max(0, col-1)
        r = min(m, col+2)
        for i in range(up, down):
            for j in range(l, r):
                if i!=row or j != col:
                    self.neighbours.append(seats[i,j])
    def occupied(self):
        occupied_seats = [n for n in self.neighbours if n == CellType.OCCUP]
        return len(occupied_seats)
        
class Seats:
    def __init__(self, conf0):
        self.seats = np.array([ [CellType(x) for x in row] for row in conf0])
        self.stable = False

    def is_stable(self):
        return self.stable

    def rearange(self):
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
            if neighbourhood.occupied() >= 4:
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
        seats.rearange()
    occupied = seats.get_occupied_seats()
    print("The number of seats occupied with the final configuration is: {}".format(occupied))
