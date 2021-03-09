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

    def single_availability(self, x, y):
        if self.grid[x][y] != 0:
            return set({})

        fullset = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        rowset = set(self.rows[x])
        columnset = set(self.columns[y])
        cell_range = self.cell[self.get_cell_number(x, y)]
        cellset = []

        for r in range(cell_range[0][0], cell_range[1][0] + 1):
            for c in range(cell_range[0][1], cell_range[1][1] + 1):
                cellset.append(self.grid[r][c])
        cellset = set(cellset)
        result = fullset.difference(rowset.union(columnset.union(cellset)))
        return result

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

    def pretty(self, full=1):
        print("\n Grid:\n")
        print("-------------------------")
        for r in range(self.n):
            print("|", end=" ")
            for c in range(self.n):
                if self.grid[r][c] != 0 or full == 1:
                    print(self.grid[r][c], end=" ")
                else:
                    print(" ", end=" ")
                if (c + 1) % 3 == 0:
                    print("|", end=" ")
            print()
            if (r + 1) % 3 == 0:
                print("-------------------------")


if __name__ == "__main__":
    a = Sudoku(sourcefile="c:/Users/rajatshr/Desktop/Code/Misc/sudoku/sudoku_input.txt")
    a.pretty(0)
    for r in range(6, 9):
        for c in range(3, 6):
            print(a.single_availability(r, c), end=" ")
        print()

