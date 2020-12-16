def two_sum(xs, s):
    d = dict()
    for x in xs:
        d[s - x] = x
    return [(x,d[x]) for x in xs if x in d]
            
def three_sum(xs, s):
    ret = []
    for x in xs:
        aux = xs[:]
        aux.remove(x)
        ret += [(x,y,z) for y,z in two_sum(aux, s-x)]
    return ret

if __name__ == "__main__":
    with open("2020_12_01.input") as f:
        numbers = [int(line.strip()) for line in f]
    sol1 = two_sum(numbers, 2020)
    for ans in sol1:
        x, y = ans
        print("x={},y={}".format(x,y))
        print("x*y={}".format(x*y))

    sol2 = three_sum(numbers, 2020)
    for ans in sol2:
        x, y, z = ans
        print("x={},y={},z={}".format(x,y,z))
        print("x*y*z={}".format(x*y*z))
    
    
