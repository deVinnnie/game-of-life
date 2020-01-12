import curses
from curses import wrapper
import copy
import random
import time
import click

class GameOfLife:

    def __init__(self, lines=1, rows=1, seed=1):
        random.seed(seed)
        self.grid = []
        self.grid = [None] * lines

        for y in range(0, lines):
            self.grid[y] = list(random.choice([True, False]) for i in range(rows))

    def number_of_neighbours(self, y, x, grid):
        # <x>
        # xxx    ^
        # x x    y
        # xxx    v

        coordinates = [
          (y-1, x-1),
          (y-1, x),
          (y-1, x+1),

          (y, x-1),
          (y, x+1),

          (y+1, x-1),
          (y+1, x),
          (y+1, x+1)
        ]
        positive_coordinates = list(filter(lambda point: point[0] >= 0 and point[1] >= 0, coordinates))
        positive_coordinates = list(filter(lambda point: point[0] < len(grid) and point[1] < len(grid[0]), positive_coordinates))

        neighbours = list(map(lambda point: self.grid[point[0]][point[1]], positive_coordinates))
        return len(list(filter(lambda cell: cell is True, neighbours)))

    def tick(self):
        new_grid = copy.deepcopy(self.grid)
        for y in range(0, len(self.grid)):
            row = self.grid[y]
            for x in range(0, len(row)):
                cell = row[x]
                number_of_neighbours = self.number_of_neighbours(y, x, self.grid)
                # 1. Any live cell with two or three neighbours survives
                if cell is True and (number_of_neighbours == 2 or number_of_neighbours == 3):
                    new_grid[y][x] = True
                # 2. Any dead cell with three live neighbours becomes a live cell:
                elif cell is False and (number_of_neighbours == 3):
                    new_grid[y][x] = True
                # 3. All other live cells die in the next generation.
                else:
                    new_grid[y][x] = False

        self.grid = new_grid

@click.command()
@click.option('--seed', default=1, type=int)
def start_curses(seed):
    wrapper(main, seed)

def main(stdscr, seed):
    stdscr.clear()

    game = GameOfLife(curses.LINES-1, curses.COLS-1, seed)

    stdscr.nodelay(True)

    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break

        game.tick()
        for y in range(0, len(game.grid)):
            row = game.grid[y]
            row = list(map(lambda cell: 'x' if cell is True else ' ', row))
            row = ''.join(row)
            stdscr.addstr(y, 0, row)

        stdscr.refresh()
        time.sleep(0.250)

if __name__ == "__main__":
    start_curses()
