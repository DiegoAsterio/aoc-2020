def count_trees_in_walk(forest, R, D):
    counter = 0
    m = len(forest)
    j = 0
    for i, row in zip(range(0,m,D), forest):
        n = len(row)
        if forest[i][j%n] == '#':
           counter += 1
        j += R
    return counter

def load_forest(path):
    with open(path) as f:
        return [line.strip() for line in f]

if __name__ == "__main__":
    forest = load_forest("2020_12_03.input")

    print("Right 3, down 1: {}".format(count_trees_in_walk(forest,3,1)))

    inputs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    prod = 1
    for R, D in inputs:
        prod *= count_trees_in_walk(forest, R, D)

    print("Product of trees is: {}".format(prod))
