from aoc.utils import local_path, get_lines

from aoc.day14.first.solution import BitMask, sum_up_values

import unittest

class TestBitMask(unittest.TestCase):
    def test_first_example(self):
        mask = BitMask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        value = 11
        result = 73
        self.assertEqual(mask.apply_mask(value),result)
    def test_second_example(self):
        mask = BitMask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        value = 101
        result = 101
        self.assertEqual(mask.apply_mask(value),result)
    def test_third_example(self):
        mask = BitMask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
        value = 0
        result = 64
        self.assertEqual(mask.apply_mask(value),result)
    def sums_up_correctly(self):
        rel_route_input = "../smallinput1"
        path = local_path(__file__, rel_route_input)

        instructions = get_lines(path)

        real_sum = 165
        self.asserEqual(sum_up_values(instructions), real_sum)
        
if __name__ == "__main__":
    unittest.main()
