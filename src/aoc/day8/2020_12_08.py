from enum import Enum, auto

class Operation(Enum):
    NOP = "nop"
    JMP = "jmp"
    ACC = "acc"

class Instruction:
    def __init__(self, op, num):
        self.op = Operation(op)
        self.num = int(num)
        
    def run(self):
        if self.op == Operation.NOP:
            dindex = 1
            dacc = 0
        if self.op == Operation.JMP:
            dindex = self.num
            dacc = 0
        if self.op == Operation.ACC:
            dindex = 1
            dacc = self.num
        return dindex, dacc

class BootCode:
    def __init__(self, instructions):
        self.instructions = instructions
        self.order = [-1 for _ in range(len(instructions))]
        self.ins_num = 0
        self.index = 0
        self.acc = 0
        self.finished = False

    def update_order(self):
        self.order[self.index] = self.ins_num
        self.ins_num += 1

    def not_finished(self):
        n = len(self.instructions)
        if self.index < n:
            return self.order[self.index] == -1
        self.finished = True
        return False

    def correctly_finished(self):
        return self.finished

    def run_bootcode(self):
        n = len(self.instructions)
        while self.not_finished():
            self.update_order()
            instruction = self.instructions[self.index]
            dindex, dacc = instruction.run()
            self.index += dindex
            self.acc += dacc
        return self.acc

def parse_instruction(line):
    op, num = line.strip().split(' ')
    return Instruction(op, num)
    
def get_data(path):
    with open(path) as f:
        ls = f.read()
    instructions = []
    for l in ls.split('\n'):
        if len(l) > 0:
            instruction = parse_instruction(l)
            instructions.append(instruction)
    return instructions

def permutable_instruction(ins):
    return ins.op == Operation.NOP or ins.op == Operation.JMP

def permute_instruction(i, instructions):
    ins = instructions[i]
    op = ins.op
    num = ins.num
    if op == Operation.NOP:
        op = Operation.JMP
    elif op == Operation.JMP:
        op = Operation.NOP
    ins = Instruction(op, num)
    instructions[i] = ins

def change_code_to_terminate(instructions):
    n = len(instructions)
    for i, ins in zip(range(n),instructions):
        if permutable_instruction(ins):
            permute_instruction(i, instructions)
            bootcode = BootCode(instructions)
            acc = bootcode.run_bootcode()
            if bootcode.correctly_finished():
                return acc
            permute_instruction(i, instructions)

if __name__ == "__main__":
    instructions = get_data("2020_12_08.input")
    bootcode = BootCode(instructions)
    acc = bootcode.run_bootcode()
    print("The accumulator before entering the infinite loop had {}".format(acc))

    acc = change_code_to_terminate(instructions)

    print("The accumulator after running the corrected program has {}".format(acc))
