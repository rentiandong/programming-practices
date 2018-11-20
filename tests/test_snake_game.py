import unittest
from snake_game import SnakeGame


class TestEvaluateDivision(unittest.TestCase):

    def test_small_0(self):
        game = SnakeGame(3, 2, [[1, 2], [0, 1]])
        moves = ['R', 'D', 'R', 'U', 'L', 'U']
        expected = [0, 0, 1, 1, 2, -1]
        for m, e in zip(moves, expected):
            self.assertEqual(e, game.move(m))

    def test_medium_0(self):
        game = SnakeGame(3, 3, [[0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0]])
        moves = ['R', 'R', 'D', 'D', 'L', 'L', 'U', 'U', 'R', 'R', 'D', 'D', 'L', 'L', 'U', 'R', 'U', 'L', 'D']
        print(game)
        for i in range(0, len(moves)):
            print()
            print(f'i: {i}, move: {moves[i]}')
            game.move(moves[i])
            print(game)
