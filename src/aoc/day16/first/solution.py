import math

import re

import attr

import pdb

from aoc.utils import local_path

@attr.s
class Range:
    a  = attr.ib(converter=int)
    b  = attr.ib(converter=int)

    def contains(self, value):
        return self.a <= value and value <= self.b

@attr.s(frozen=True)
class Rule:
    first_range = attr.ib(converter=lambda x: Range(*x))
    second_range = attr.ib(converter=lambda x: Range(*x))
    name = attr.ib()

    def holds(self, value):
        return self.first_range.contains(value) or self.second_range.contains(value)

def parse_rule(rule_info):
    rule_name_re = r"(?P<name>\D+): "
    range_re = r"(?P<min>\d+)-(?P<max>\d+)"

    return Rule(*re.findall(range_re, rule_info),
                **re.match(rule_name_re, rule_info).groupdict())

def parse_rules(rules_info):
    return [parse_rule(rule_info) for rule_info in rules_info.split('\n')]

def parse_ticket(ticket_values):
    return [int(x) for x in ticket_values.strip().split(',')]

def parse_your_ticket(your_ticket_info):
    _your_ticket, ticket_values = your_ticket_info.strip().split('\n')
    assert (_your_ticket == "your ticket:"), "Parsing your ticket incorrectly"
    return parse_ticket(ticket_values)

def parse_nearby_tickets(nearby_tickets_info):
    nearby_tickets_it = iter(nearby_tickets_info.strip().split('\n'))
    _nearby_tickets = nearby_tickets_it.__next__()
    assert (_nearby_tickets == "nearby tickets:"), "Parsing nearby tickets incorrectly"
    return [parse_ticket(ticket_values) for ticket_values in nearby_tickets_it]

def parse_input(path):
    with open(path) as f:
        rules_info, your_ticket_info, nearby_tickets_info = f.read().split('\n\n')
    rules = parse_rules(rules_info)
    your_ticket = parse_your_ticket(your_ticket_info)
    nearby_tickets = parse_nearby_tickets(nearby_tickets_info)
    return rules, your_ticket, nearby_tickets

def sum_up_not_valid_values(rules, nearby_tickets):
    nearby_tickets_values = [x for ticket in nearby_tickets for x in ticket]
    return sum(x
               for x in nearby_tickets_values
               if not any(rule.holds(x) for rule in rules))

def main():
    to_input = "../input"
    path = local_path(__file__, to_input)

    rules, _, nearby_tickets = parse_input(path)
    
    print(sum_up_not_valid_values(rules, nearby_tickets))

if __name__ == "__main__":
    main()
