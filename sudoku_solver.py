import numpy as np


class Sudoku:
    def __init__(self):
        self.rank = 3
        self.n = self.rank ** 2
        # self.grid = np.zeros((n,n), dtype=np.uint8) #real
        self.grid = np.uint8(np.random.rand(self.n, self.n) * 10)
        self.rows = np.array([x for x in self.grid])
        self.columns = self.grid.T

    def display(self):
        print("Grid:")
        print(self.grid)
        print("Rows:")
        print(self.rows)
        print("Columns:")
        print(self.columns)


a = Sudoku()
a.display()

