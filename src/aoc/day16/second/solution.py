import re

from functools import reduce
from operator import mul
from itertools import product

from aoc.utils import local_path

from aoc.day16.first.solution import Rule, parse_input

import pdb

class NonOverlappingName:
    def __init__(self, names):
        self.names = names
        self.finished = False
        self.solution = None

    def is_solution(self, partial_solution):
        return len(partial_solution) == len(self.names)

    def process_solution(self, partial_solution):
        self.solution = partial_solution
        self.finished = True

    def get_candidates(self, used_names, partial_solution):
        n = len(partial_solution)
        return (name
                for name in self.names[n]
                if name not in used_names)
        
    def backtrack_with_prune(self, used_names, partial_solution):
        if self.is_solution(partial_solution):
            self.process_solution(partial_solution)
        else:
            candidates = self.get_candidates(used_names, partial_solution)
            for candidate in candidates:
                self.backtrack_with_prune(used_names | {candidate},
                                          partial_solution + [candidate])
                if self.finished:
                    break
                
    def get_non_overlapping_name(self):
        self.backtrack_with_prune(set(), [])
        return self.solution
        
        
def ticket_is_valid(ticket, rules):
    return all(any(rule.holds(x) for rule in rules) for x in ticket)

def valid_tickets(rules, valid_tickets):
    return [ticket
            for ticket in valid_tickets
            if ticket_is_valid(ticket, rules)]
        
def rules_sat(rules, values):
    rules_sat = rules[:]
    for value in values:
        rules_sat = [rule
                     for rule in rules_sat
                     if rule.holds(value)]
    return rules_sat

def non_overlapping_name(rules_each_field):
    fieldname_options = [[rule.name for rule in rules]
                         for rules in rules_each_field]
    name = NonOverlappingName(fieldname_options)
    ret = name.get_non_overlapping_name()
    return ret

def non_overlapping_name_using_chain_property(rules_each_field):
    fieldname_options = [(i,[rule.name for rule in rules])
                         for i, rules in enumerate(rules_each_field)]
    fieldname_options_chain = sorted(fieldname_options, key=lambda x: len(x[1]))
    solution = []
    used_names = set()
    for i, names in fieldname_options_chain:
        for name in names:
            if name not in used_names:
                solution.append((i,name))
                used_names.add(name)
    ret= list(map(lambda x: x[1],
                  sorted(solution,
                         key= lambda x: x[0])))
    return ret

def fieldnames(rules, valid_tickets):
    # We transpose the matrix; now each field is a row
    values_in_each_field = zip(*valid_tickets)
    rules_satisfied = [rules_sat(rules, values)
                       for values in values_in_each_field]
    return non_overlapping_name_using_chain_property(rules_satisfied)

def starting_with(fieldnames, word):
    starting_re = r"^"+word
    ret = []
    for i, name in enumerate(fieldnames):
        m = re.match(starting_re, name)
        if m:
            ret.append(i)
    return ret

def multiply_departure(rules, your_ticket, nearby_tickets):
    valid = valid_tickets(rules, nearby_tickets)
    names = fieldnames(rules, valid)

    indices = starting_with(names, "departure")
    return reduce(mul,
                  (your_ticket[i]
                   for i in indices))

def main():
     to_input = "../input"
     path = local_path(__file__, to_input)
     
     my_input = parse_input(path)
        
     print(multiply_departure(*my_input))

if __name__ == '__main__':
    main()
    
