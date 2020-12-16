from aoc.utils import local_path, find, get_lines

from aoc.day15.first.solution import ElfGame, get_nth_value
            
def main():
    rel_route_input = "../input"
    path = local_path(__file__, rel_route_input)

    values = [int(x) for x in get_lines(path)[0].split(',')]

    print(get_nth_value(values, 30000000))

if __name__ == '__main__':
    main()
