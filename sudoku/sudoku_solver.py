import numpy as np


class Sudoku:
    def __init__(self, rank=3, sourcefile=False):
        self.rank = rank
        self.filename = sourcefile
        self.n = self.rank ** 2
        self.cell = {}
        x, y = 0, 0
        for i in range(self.n):
            self.cell[i] = [(x, y), (x + self.rank - 1, y + self.rank - 1)]
            y += self.rank
            if y == self.n:
                y = 0
                x += self.rank

        if self.filename:
            self.grid = self._input()
        else:
            print(" No source file provided. Init to zero by default. ")
            self.grid = np.zeros((self.n, self.n), dtype=np.uint8)

        self._syncgrid()

    def _syncgrid(self):
        self.rows = np.array([x for x in self.grid])
        self.columns = self.grid.T

    def get_cell_number(self, x, y):
        x = x // self.rank
        y = y // self.rank
        return x * 3 + y

    def _input(self):
        if self.filename:
            with open(self.filename) as file:
                data = file.readlines()
                r = []
                for line in data:
                    if line == "\n":
                        break
                    r.append(list(line.split()[0]))
                return np.array(r, dtype=np.uint8)
        else:
            print(" Invalid syntax for input(). Enter source filename \n")
        return 0

    def display(self):
        print("Grid:")
        print(self.grid)
        print(" Shape: ", self.grid.shape)


if __name__ == "__main__":
    a = Sudoku(sourcefile="c:/Users/rajatshr/Desktop/Code/Misc/sudoku/sudoku_input.txt")
    a.display()
    print()
    for r in range(a.n):
        for c in range(a.n):
            print(a.cell[a.get_cell_number(r, c)], end=" ")
        print()

