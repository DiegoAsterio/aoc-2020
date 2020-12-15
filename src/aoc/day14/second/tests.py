from aoc.utils import local_path, get_lines
from aoc.day14.second.solution import MemoryAddressDecoder, write_memory

import unittest

class TestMemoryAddressDecoder(unittest.TestCase):
    def test_first_example(self):
        decoder = MemoryAddressDecoder('000000000000000000000000000000X1001X')
        value = 42
        addresses = [26, 27, 58, 59]
        self.assertEqual(decoder.decode(value), addresses)

    def test_second_example(self):
        decoder = MemoryAddressDecoder('00000000000000000000000000000000X0XX')
        value = 26
        addresses = [16, 17, 18, 19, 24, 25, 26, 27]
        self.assertEqual(decoder.decode(value), addresses)

    def test_sums_correctly(self):
        rel_route_input = '../smallinput'
        path = local_path(__file__, rel_route_input)

        instructions = get_lines(path)

        mem = write_memory(instructions)

        s = sum(mem.values())
        actual_sum = 208
        
        self.assertEqual(s, actual_sum)
        
if __name__ == '__main__':
    unittest.main()
