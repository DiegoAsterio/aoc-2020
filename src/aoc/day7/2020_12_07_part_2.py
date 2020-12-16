import pdb

import parse
import re

def get_tree_contains(path):
    bagcode = r"[ ]*(?P<number>\d+) (?P<colorcode>[a-z ]+) bag(?P<plural>s?)"
    dag = dict()
    with open(path) as f:
        for line in f:
            r = parse.parse("{container} bags contain {contained}.", line)
            container = r['container']
            for contained in r['contained'].split(','):
                match = re.match(bagcode, contained)
                if match is not None:
                    color_contained = match.group('colorcode')
                    number_of_elems = int(match.group('number'))
                    if container in dag: 
                        dag[container][color_contained] = number_of_elems
                    else:
                        dag[container] = {color_contained: number_of_elems}
                else:
                    dag[container] = {}
    return dag

def count_bags_inside(bag_name, dag, acc=1):
    if len(dag[bag_name])==0:
        return 1
    else:
        for k in dag[bag_name]:
            n = dag[bag_name][k]
            acc += n*count_bags_inside(k, dag)
        return acc

if __name__ == "__main__":
    path = "2020_12_07.input"

    dag = get_tree_contains(path)
    n = count_bags_inside('shiny gold', dag, 0)
    print(n)
