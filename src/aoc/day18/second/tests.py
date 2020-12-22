from aoc.day18.first.solution import shunting_yard_alg, solve_rpn

import unittest

class TestSolveExpressionTree(unittest.TestCase):
    def setUp(self):
        self.prec = {'+': 2, '*': 1}

    def test_first_example(self):
        expr = '1 + (2 * 3) + (4 * (5 + 6))'
        rpn = shunting_yard_alg(expr, self.prec)

        should_be = 51
        self.assertEqual(solve_rpn(rpn),
                         should_be)

    def test_second_example(self):
        expr = '2 * 3 + (4 * 5)'
        rpn = shunting_yard_alg(expr, self.prec)

        should_be = 46
        self.assertEqual(solve_rpn(rpn),
                         should_be)

    def test_third_example(self):
        expr = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
        rpn = shunting_yard_alg(expr, self.prec)

        should_be = 1445
        self.assertEqual(solve_rpn(rpn),
                         should_be)

    def test_fourth_example(self):
        expr = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
        rpn = shunting_yard_alg(expr, self.prec)

        should_be = 669060
        self.assertEqual(solve_rpn(rpn),
                         should_be)

    def test_fifth_example(self):
        expr = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
        rpn = shunting_yard_alg(expr, self.prec)

        should_be = 23340
        self.assertEqual(solve_rpn(rpn),
                         should_be)

        
if __name__ == '__main__':
    unittest.main()
