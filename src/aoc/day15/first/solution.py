from aoc.utils import local_path, find, get_lines

class ElfGame:
    def __init__(self, xs):
        self.when_did_we_speak_about = dict()
        for i, x in enumerate(xs[:-1]):
            turn = i + 1
            self.when_did_we_speak_about[x] = turn
        self.turn = len(xs)
        self.last_number_spoken = xs[-1]
        
    def this_turn_number(self):
        ret = 0
        if self.last_number_spoken in self.when_did_we_speak_about:
            turn_last_spoken = self.when_did_we_speak_about[self.last_number_spoken]
            ret = self.turn - turn_last_spoken
        return ret    

    def remember_last_number_spoken(self):
        self.when_did_we_speak_about[self.last_number_spoken] = self.turn 

    def next_turn(self):
        this_turn_number = self.this_turn_number()
        self.remember_last_number_spoken()
        
        self.last_number_spoken = this_turn_number
        self.turn += 1

    def advance_to_turn(self,n):
        while self.turn < n:
            self.next_turn()

def get_nth_value(values, n):
    game = ElfGame(values)

    game.advance_to_turn(n)

    return(game.last_number_spoken)

def get_values(path):
    with open(path) as f:
        line = f.read().strip()
    return list(map(int, line.split(',')))
        
def main():
    rel_route_input = "../input"
    path = local_path(__file__, rel_route_input)

    values = get_values(path)

    print(get_nth_value(values, 2020))

if __name__ == "__main__":
    main()

    
