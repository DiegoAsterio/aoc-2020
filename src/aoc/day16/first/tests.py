import unittest

from aoc.utils import local_path

from .solution import parse_input, sum_up_not_valid_values

class TestScanningErrorRate(unittest.TestCase):
    def test_first_example(self):
        to_input = "../smallinput"
        path = local_path(__file__, to_input)

        rules, _, nearby_tickets = parse_input(path)
        
        should_be = 71
        self.assertEqual(should_be,
                         sum_up_not_valid_values(rules, nearby_tickets))

if __name__ == "__main__":
    unittest.main()
