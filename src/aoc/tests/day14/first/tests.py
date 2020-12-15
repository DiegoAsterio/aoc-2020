from .solution import BitMask

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
        
if __name__ == "__main__":
    unittest.main()
