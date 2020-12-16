import unittest

from aoc.day15.first.solution import ElfGame

class TestElfGame(unittest.TestCase):
    def test_first_example(self):
        my_game = ElfGame([0,3,6])
        my_game.advance_to_turn(10)
        should_be = 0
        self.assertEqual(my_game.last_number_spoken, should_be)

    def test_second_example(self):
        my_game = ElfGame([1,3,2])
        my_game.advance_to_turn(2020)
        should_be = 1
        self.assertEqual(my_game.last_number_spoken, should_be)

    def test_third_example(self):
        my_game = ElfGame([2,1,3])
        my_game.advance_to_turn(2020)
        should_be = 10
        self.assertEqual(my_game.last_number_spoken, should_be)

    def test_fourth_example(self):
        my_game = ElfGame([1,2,3])
        my_game.advance_to_turn(2020)
        should_be = 27
        self.assertEqual(my_game.last_number_spoken, should_be)

    def test_fifth_example(self):
        my_game = ElfGame([2,3,1])
        my_game.advance_to_turn(2020)
        should_be = 78
        self.assertEqual(my_game.last_number_spoken, should_be)

    def test_sixth_example(self):
        my_game = ElfGame([3,2,1])
        my_game.advance_to_turn(2020)
        should_be = 438
        self.assertEqual(my_game.last_number_spoken, should_be)

if __name__ == '__main__':
    unittest.main()
