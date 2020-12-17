import unittest

from aoc.utils import local_path

from aoc.day16.first.solution import parse_input
from aoc.day16.second.solution import valid_tickets, fieldnames

class TestFindingNames(unittest.TestCase):
    def test_first_example(self):
        to_input = "../smallinput2"
        path = local_path(__file__, to_input)

        rules, _, nearby_tickets = parse_input(path)
        valid = valid_tickets(rules, nearby_tickets)
        
        should_be = ["row","class","seat"]
        self.assertEqual(fieldnames(rules,
                                    valid),
                         should_be)

if __name__ == "__main__":
    unittest.main()
