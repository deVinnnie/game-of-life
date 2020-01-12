import unittest

from main import GameOfLife

class NeighbourTest(unittest.TestCase):
    def test_gives_correct_result_1(self):
        game = GameOfLife()
        game.grid = [
                [True, True, True],
                [True, True, True],
                [True, True, True]
               ]

        self.assertEqual(
            game.number_of_neighbours(1, 1, game.grid),
            8
        )

    def test_gives_correct_result_2(self):
        game = GameOfLife()
        game.grid = [
                [False, False, False],
                [False, False, False],
                [False, False, False]
               ]

        self.assertEqual(
            game.number_of_neighbours(1, 1, game.grid),
            0
        )


    def test_doesnt_crash_on_edges1(self):
        game = GameOfLife()
        game.grid = [
                [True, False, False],
                [True, False, False],
                [True, False, False]
               ]

        self.assertEqual(
            game.number_of_neighbours(0, 0, game.grid),
            1
        )

    def test_doesnt_crash_on_edges2(self):
        game = GameOfLife()
        game.grid = [
                [False, False, False],
                [False, True, True],
                [False, True, False]
               ]

        self.assertEqual(
            game.number_of_neighbours(2, 2, game.grid),
            3
        )

    def test_doesnt_crash_on_edges2(self):
        game = GameOfLife()
        game.grid = [
                [False, False, False],
                [False, True, True],
                [False, False, False]
               ]

        self.assertEqual(
            game.number_of_neighbours(0, 2, game.grid),
            2
        )

class TickTest(unittest.TestCase):
    def setUp(self):
        self.game = GameOfLife()

    def test_live_cells_with_two_neighbours_survives(self):
        self.game.grid = [
            [False, True, False],
            [False, True, False],
            [False, True, False],
        ]
        self.game.tick()
        self.assertEqual(
            self.game.grid[1][1],
            True
        )

    def test_live_cells_with_three_neighbours_survives(self):
        self.game.grid = [
            [False, True, False],
            [False, True, True],
            [False, True, False],
        ]
        self.game.tick()
        self.assertEqual(
            self.game.grid[1][1],
            True
        )

    def test_dead_cells_with_three_neighbours_become_alive(self):
        self.game.grid = [
            [False, True, False],
            [False, False, True],
            [False, True, False],
        ]
        self.game.tick()
        self.assertEqual(
            self.game.grid[1][1],
            True
        )

    def test_live_cells_with_no_neighbours_dies(self):
        self.game.grid = [
            [False, False, False],
            [False, True, False],
            [False, False, False],
        ]
        self.game.tick()
        self.assertEqual(
            self.game.grid[1][1],
            False
        )

    def test_live_cells_with_single_neighbour_dies(self):
        self.game.grid = [
            [False, False, False],
            [True, True, False],
            [False, False, False],
        ]
        self.game.tick()
        self.assertEqual(
            self.game.grid[1][1],
            False
        )

    def test_live_cells_with_four_neighbours_dies(self):
        self.game.grid = [
            [True, True, True],
            [True, True, False],
            [False, False, False],
        ]
        self.game.tick()
        self.assertEqual(
            self.game.grid[1][1],
            False
        )

class GridInitTest(unittest.TestCase):
    def test_grid_init(self):
        game = GameOfLife(3, 5)
        self.assertEqual(len(game.grid), 3)
        self.assertEqual(len(game.grid[0]), 5)
