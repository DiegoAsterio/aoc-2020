from collections import deque

def two_sum(xs, s):
    d = dict()
    for x in xs:
        d[s - x] = x
    return [(x,d[x]) for x in xs if x in d]

def get_numbers(path):
    with open(path) as f:
        return [int(x) for x in f.read().strip().split('\n')]

def find_exploit(xs):
    preamble = deque([])
    for i, x in enumerate(xs):
        if i < preamble_size:
            preamble.append(x)
        else:
            pairs_that_add_x = two_sum(preamble, x)
            if not pairs_that_add_x:
                return x
            preamble.append(x)
            preamble.popleft()
            
def find_range_that_adds(exploit, xs):
    l = 0
    r = 2
    s = sum(xs[l: r])
    while l < len(xs) and r < len(xs) + 1:
        if s < exploit:
            s += xs[r]
            r += 1
        elif s > exploit:
            s -= xs[l]
            l += 1
        if s == exploit:
            return xs[l:r]
    
if __name__ == '__main__':
    preamble_size = 25
    path = '2020_12_09.input'
    xs = get_numbers(path)
    exploit = find_exploit(xs)
    print('The first number that can be exploited is {}'.format(exploit))

    range_that_adds_exploit = find_range_that_adds(exploit, xs)

    minimum = min(range_that_adds_exploit)
    maximum = max(range_that_adds_exploit)
    weakness = minimum + maximum
    print('The encryption weakness is {}'.format(weakness))

