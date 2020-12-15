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

def mask_values(instructions):
    mask_re = re.compile("mask = (?P<definition>[01X]{36})$")
    memw_re = re.compile("mem\[(?P<index>\d+)\] = (?P<value>\d+)$")

    mask = None
    values_to_mask = []
    for inst in instructions:
        mask_m = mask_re.match(inst)
        if mask_m:
            if mask:
                yield mask, values_to_mask
                values_to_mask = []
            definition = mask_m.group('definition')
            mask = definition
        mem_m = memw_re.match(inst)
        if mem_m:
            index = int(mem_m.group('index'))
            value = int(mem_m.group('value'))
            values_to_mask.append((index, value))
    yield mask, values_to_mask

def write_memory(instructions):
    mem = dict()

    for definition, values in mask_values(instructions):
        for index, number in values:
            mask = BitMask(definition)
            mem[index] = mask.apply_mask(number)
    return mem

def sum_up_values(instructions):
    mem = write_memory(instructions)

    return sum(mem.values())
    

def main():
    rel_route_input = "../input"
    path = local_path(__file__, rel_route_input)

    instructions = get_lines(path)

    print(sum_up_values(instructions))

if __name__ == "__main__":
    main()
