import numpy as np


class Sudoku:
    def __init__(self, rank=3, sourcefile=False):
        self.rank = rank
        self.filename = sourcefile
        self.n = self.rank ** 2
        if self.filename:
            self.grid = self._input()
        else:
            print(" No source file provided. Init to zero by default. ")
            self.grid = np.zeros((self.n, self.n), dtype=np.uint8)

        self._syncgrid()

    def _syncgrid(self):
        self.rows = np.array([x for x in self.grid])
        self.columns = self.grid.T

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

