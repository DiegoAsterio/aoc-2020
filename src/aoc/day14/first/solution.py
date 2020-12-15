from aoc.utils import local_path, get_lines

import re

class BitMask:
    def __init__(self, definition):
        self.or_mask = sum(2**i for i, x in enumerate(reversed(definition)) if x == '1')
        self.and_mask = sum(2**i for i, x in enumerate(reversed(definition)) if x != '0')

    def apply_mask(self, value):
        ret = value | self.or_mask
        ret = ret & self.and_mask
        return ret

def write_memory(instructions):
    mem = dict()

    mask_re = re.compile("mask = (?P<definition>[01X]{36})$")
    memw_re = re.compile("mem\[(?P<index>\d+)\] = (?P<value>\d+)$")
    
    for inst in instructions:
        mask_m = mask_re.match(inst)
        if mask_m:
            definition = mask_m.group('definition')
            mask = BitMask(definition)
        mem_m = memw_re.match(inst)
        if mem_m:
            index = mem_m.group('index')
            value = int(mem_m.group('value'))
            mem[index] = mask.apply_mask(value)
    return mem

def main():
    rel_route_input = "../input"
    path = local_path(__file__, rel_route_input)

    instructions = get_lines(path)

    mem = write_memory(instructions)

    s = sum(mem.values())
    sol_st = 'The sum of all values after the initialization program completes is {}'
    print(sol_st.format(s))

if __name__ == "__main__":
    main()
