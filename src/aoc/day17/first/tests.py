import unittest

from aoc.utils import local_path, get_lines
from aoc.day17.first.solution import count_living_cells

class TestBoard(unittest.TestCase):
    def test_first_example(self):
        to_input = "../smallinput"
        path = local_path(__file__, to_input)

        config = get_lines(path)

        should_be = 112
        self.assertEqual(count_living_cells(config),
                         should_be)

if __name__ == "__main__":
    unittest.main()
    
