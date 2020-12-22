from aoc.utils import local_path, get_lines

from aoc.day18.first.solution import sum_exprs

def main():
    to_input = "../input"
    path = local_path(__file__, to_input)

    prec = {'+': 2, '*': 1}
    print(sum_exprs(get_lines(path), prec))

if __name__ == '__main__':
    main()
