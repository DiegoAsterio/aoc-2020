import re
from itertools import product

from aoc.day14.first.solution import BitMask
from aoc.utils import local_path, get_lines, find

class MemoryAddressDecoder:
    def __init__(self, definition):
        self.definition = definition
        floating_indices = find(definition, 'X')
        floating_bits = self.get_floating_bits(floating_indices)
        self.masks = []
        for bit_combination in floating_bits:
            indexing_mask = self.create_mask(floating_indices, bit_combination)
            self.masks.append(indexing_mask)

    def get_floating_bits(self, floating_indices):
        n = len(floating_indices)
        return product("01", repeat = n)   # ...000, ...001, ...010, ...
            
    def create_mask(self, floating_indices, bit_combination):
        base_mask = self.definition.replace('0', 'X')
        zip_index_bit = zip(floating_indices, bit_combination)
        replacement = {i: bit
                       for i, bit in zip_index_bit}
        mask_definition = ''.join(replacement[i] if i in replacement else x
                                  for i, x in enumerate(base_mask))
        return BitMask(mask_definition)
        
    def decode(self, address):
        return [mask.apply_mask(address) for mask in self.masks]


    
def write_memory(instructions):
    mem = dict()

    mask_re = re.compile("mask = (?P<definition>[01X]{36})$")
    memw_re = re.compile("mem\[(?P<index>\d+)\] = (?P<value>\d+)$")

    for decoder, values in decoder_values(instructions):
        for index, number in values:
            for address in decoder.decode(index):
                mem[address] = number
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
