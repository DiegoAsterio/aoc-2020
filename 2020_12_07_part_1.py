import pdb

import parse
import re

def succ_bfs(succ,cand,tree):
    if len(cand) == 0:
        return succ
    else:
        aux = []
        for y in cand:
            if y in tree:
                aux += list(tree[y])
        succ |= set(aux)
        return succ_bfs(succ, aux, tree)

if __name__ == "__main__":
    bagcode = r"[ ]*(?P<number>\d+) (?P<colorcode>[a-z ]+) bag(?P<plural>s?)"
    dag = dict()
    with open("2020_12_07.input") as f:
        for line in f:
            r = parse.parse("{container} bags contain {contained}.",line)
            container = r['container']
            for contained in r['contained'].split(','):
                match = re.match(bagcode, contained)
                if match is not None:
                    color_contained = match.group('colorcode')
                    if color_contained in dag: 
                        dag[color_contained].add(container)
                    else:
                        dag[color_contained] = {container}
                else:
                    print(contained)
    outter_envelopes = succ_bfs(set(), ['shiny gold'], dag)
    print(outter_envelopes)
    print(len(outter_envelopes))
                
