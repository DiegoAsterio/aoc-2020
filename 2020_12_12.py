import numpy as np

import pdb

class Boat:
    def __init__(self):
        self.position = np.array([[0],[0]])
        self.dir = np.array([[1], [0]])

    def move(self, movement):
        if movement.is_turn():
            self.dir = movement.turn(self.dir)
        elif movement.is_increment():
            self.position += movement.steps*self.dir
        else:
            self.position += movement.steps*movement.vec

    def manhattan_distance(self):
        return sum(abs(x) for x in self.position.flatten())

class Movement:
    def __init__(self, direction, steps):
        self.direction = direction
        self.steps = steps
        self.vec = self.get_dv(direction)
    def is_turn(self):
        return self.direction == 'R' or self.direction == 'L'
    def turn(self, dv):
        times = self.steps//90
        turn = np.array([[1, 0],
                         [0, 1]])
        if self.direction == 'R':
            for _ in range(times):
                turn = np.array([[0, 1],
                                 [-1, 0]]) @ turn 
        elif self.direction == 'L':
                turn = np.array([[0, -1],
                                 [1, 0]]) @ turn 
        return turn @ dv
    
    def is_increment(self):
        return self.direction == 'F'
    def get_dv(self, direction):
        dv = None
        if self.direction == 'N':
            dv = np.array([[0], [1]])
        elif self.direction == 'E':
            dv = np.array([[1], [0]])
        elif self.direction == 'S':
            dv = np.array([[0], [-1]])
        elif self.direction == 'W':
            dv = np.array([[-1], [0]])
        return dv
    
def load_route(path):
    with open(path) as f:
        lines = f.read().strip().split('\n')
    route = []
    for line in lines:
        route.append(Movement(line[:1],int(line[1:])))
    return route

if __name__ == "__main__":
    path = "2020_12_12.input"
    route = load_route(path)
    boat = Boat()
    for movement in route:
        boat.move(movement)
    d  = boat.manhattan_distance()
    print("After the route the manhattan distance between (0, 0) and the final point is {}".format(d))
    
