import re
from itertools import product

from aoc.day14.first.solution import BitMask
from aoc.utils import local_path, get_lines, find

class MemoryAddressDecoder:
    def __init__(self, definition):
        floating_indices = find(definition, 'X')
        base_mask = definition.replace('0', 'X')
        n = len(floating_indices)
        floating_bits = product("01", repeat = n)   # ...000, ...001, ...010, ...
        self.masks = []
        for bit_combination in floating_bits:
            zip_index_bit = zip(floating_indices, bit_combination)
            replacement = {i: bit for i, bit in zip_index_bit}
            gen_mask = (replacement[i] if i in replacement else x for i, x in enumerate(base_mask))
            mask_definition = ''.join(gen_mask)
            mask = BitMask(mask_definition)
            self.masks.append(mask)
    def decode(self, address):
        return [mask.apply_mask(address) for mask in self.masks]

def write_memory(instructions):
    mem = dict()

    mask_re = re.compile("mask = (?P<definition>[01X]{36})$")
    memw_re = re.compile("mem\[(?P<index>\d+)\] = (?P<value>\d+)$")
    
    for inst in instructions:
        mask_m = mask_re.match(inst)
        if mask_m:
            definition = mask_m.group('definition')
            decoder = MemoryAddressDecoder(definition)
        mem_m = memw_re.match(inst)
        if mem_m:
            index = int(mem_m.group('index'))
            value = int(mem_m.group('value'))
            for n in decoder.decode(index):
                mem[n] = value
    return mem

def main():
    rel_route_input = '../input'
    path = local_path(__file__, rel_route_input)

    instructions = get_lines(path)

    mem = write_memory(instructions)

    s = sum(mem.values())
    print("The sum of all values after program completes is {}".format(s))

if __name__ == "__main__":
    main()
