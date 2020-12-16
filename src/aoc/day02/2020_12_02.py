class condition:
    def __init__(self, min, max, char):
        self.min = min
        self.max = max 
        self.char = char

class password_policy:
    def __init__(self,cond, password):
        self.cond = cond
        self.password = password

    def is_valid_first_policy(self):
        appears = 0
        for c in self.password:
            if c == self.cond.char:
                appears += 1
        return self.cond.min <= appears and self.cond.max >= appears

    def is_valid_snd_policy(self):
        i = self.cond.min - 1
        j = self.cond.max - 1
        char = self.cond.char

        ocurrs = 0

        if self.password[i] == char:
            ocurrs += 1
        if self.password[j] == char:
            ocurrs += 1
        
        return ocurrs == 1

    
def line_to_pp(line):
    for_cond, password = line.rstrip().split(':')
    ab, char = for_cond.split(' ')
    a, b = ab.split('-')
    cond = condition(int(a), int(b), char)
    return password_policy(cond, password.strip())

def load_input(path):
    with open(path) as f:
        return [l for l in f]

if __name__ == "__main__":
    path = "2020_12_02.input"

    inp = load_input(path)

    pps = [line_to_pp(line) for line in inp]

    are_valid_pps = [pp.is_valid_first_policy() for pp in pps]

    print(are_valid_pps.count(True))

    are_valid_pps2 = [pp.is_valid_snd_policy() for pp in pps]
    
    print(are_valid_pps2.count(True))
