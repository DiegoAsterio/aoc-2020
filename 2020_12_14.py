import re

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
        
class BitMask:
    def __init__(self, definition):
        self.or_mask = sum(2**i for i, x in enumerate(reversed(definition)) if x == '1')
        self.and_mask = sum(2**i for i, x in enumerate(reversed(definition)) if x != '0')

    def apply_mask(self, value):
        ret = value | self.or_mask
        ret = ret & self.and_mask
        return ret

if __name__ == "__main__":
    path = "2020_12_14.input"

    memo = dict()
    
    mask_re = re.compile("mask = (?P<definition>[01X]{36})$")
    memw_re = re.compile("mem\[(?P<index>\d+)\] = (?P<value>\d+)$")
    with open(path) as f:
        mask = None
        for line in f:
            mask_m = mask_re.match(line)
            if mask_m:
                definition = mask_m.group('definition')
                mask = BitMask(definition)
            mem_m = memw_re.match(line)
            if mem_m:
                index = mem_m.group('index')
                value = int(mem_m.group('value'))
                memo[index] = mask.apply_mask(value)
    s = sum(memo.values())
    print(s)
