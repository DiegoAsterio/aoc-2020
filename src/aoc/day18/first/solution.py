from aoc.utils import local_path, get_lines

from enum import Enum

from collections import deque

import pdb

class Operator(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'

    def apply(self, x, y):
        if self.name == 'ADD':
            return x + y
        if self.name == 'SUB':
            return x - y
        if self.name == 'MUL':
            return x * y
        if self.name == 'DIV':
            return x / y

def shunting_yard_alg(tokens, prec):
    values, operators = deque(), deque()
    for token in tokens:
        if token.isnumeric():
            values.append(token)
        elif token in "+*":
            while operators and operators[-1] != '(' and prec[token] <= prec[operators[-1]]:
                op = operators.pop()
                values.append(op)
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                op = operators.pop()
                values.append(op)
            operators.pop()
    while operators:
        op = operators.pop()
        values.append(op)
    return values

def solve_rpn(tokens):
    result = deque()
    for token in tokens:
        if token.isnumeric():
            result.append(int(token))
        else:
            op = Operator(token)
            operand2 = result.pop()
            operand1 = result.pop()
            res = op.apply(operand1, operand2)
            result.append(res)
    return result.pop()

def sum_exprs(exprs, prec):
    return sum(solve_rpn(shunting_yard_alg(expr, prec))
               for expr in exprs)
    
def main():
    to_input = "../input"
    path = local_path(__file__, to_input)

    prec = {'+': 1, '*': 1}
    print(sum_exprs(get_lines(path), prec))
                     
if __name__ == "__main__":
    main()
