import numpy as np
import logging


class Sudoku:
    def __init__(self, rank=3, sourcefile=False):
        # initial call to create sudoku object
        logging.info("creating sudoku")
        self.rank = rank
        self.filename = sourcefile
        self.n = self.rank ** 2
        self.cell = {}  # contains cell number: coordinate range of cell
        x, y = 0, 0

        # find cell range for each cell
        for i in range(self.n):
            self.cell[i] = [(x, y), (x + self.rank - 1, y + self.rank - 1)]
            y += self.rank
            if y == self.n:
                y = 0
                x += self.rank

        # source for grid values
        if self.filename:
            logging.info(f" using file: {self.filename}")
            self.grid = self._input()
        else:
            logging.warning("No source file provided to init")
            print(" No source file provided. Init to zero by default. ")
            self.grid = np.zeros((self.n, self.n), dtype=np.uint8)

        # sync row and column variables
        self._syncgrid()

    def _syncgrid(self):
        # get rows and columns as variables from grid
        self.rows = np.array([x for x in self.grid])
        self.columns = self.grid.T
        logging.debug("SYNCGRID")

    def _input(self):
        # takes raw input into grid from a source file specified during init
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
            logging.error("No source file provided to _input()")
            print(" Invalid syntax for input(). Enter source filename \n")
        return 0

    def validate(self):
        self._syncgrid()

        for i in range(self.n):
            for j in range(self.n):
                if (
                    self.grid[i][j] == 0
                    and len(self.get_position_available_set(i, j)) == 0
                ):
                    logging.info(f"No numbers available at position {i},{j}")
                    return False

        for i in range(self.n):
            r = self.rows[i]
            c = self.columns[i]
            if sum(r) != sum(set(r)):
                logging.info(f"Row duplicate: {i}")
                return False
            if sum(c) != sum(set(c)):
                logging.info(f"Column duplicate: {i}")
                return False
            b = self.get_number_block(i)
            if sum(b) != sum(set(b)):
                logging.info(f"Block duplicate: {i}")
                return False
        logging.info("validation: ok")
        return True

    def solve_backtrack(self, x=0, y=0):
        """
        values = get_position_available_set() # this has all the possible values for x,y
        # values should update with the grid

        if values > 0:
            for loop in values:
                put value in x,y
                v = validate
                if v = true:
                    if last:
                        return success
                    else:
                        x,y success
                        g = go ahead
                        if g = success:
                            return success
                else:
                    failure retry loop
            confirm all loop values failed
            put 0 in x,y
            return failure
        else:
            if last:
                return success
            else:
                g = go next
                return g
        
        """
        print(f" pos: {x} {y}")
        values = self.get_position_available_set(x, y)
        next_y = y + 1
        if next_y == 9:
            next_y = 0
            next_x = x + 1
        else:
            next_x = x

        if len(values) > 0:
            for val in values:
                self.grid[x][y] = val
                v = self.validate()
                if v == True:
                    if x == 8 and y == 8:
                        return "Success"
                    else:
                        result = self.solve_backtrack(next_x, next_y)
                        if result == "Success":
                            return result
                else:
                    continue
            self.grid[x][y] = 0
            return "Failure"
        else:
            if x == 8 and y == 8:
                return "Success"
            else:
                result = self.solve_backtrack(next_x, next_y)
                return result

    def get_position_available_set(self, x, y):
        # sync to latest value
        self._syncgrid()

        # return a set of all possible values for a position x,y
        if self.grid[x][y] != 0:
            return set({})

        # set of row, column and cell block numbers
        fullset = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        rowset = set(self.rows[x])
        columnset = set(self.columns[y])
        cell_range = self.get_cell_coord(x, y)
        cellset = []

        # get cellset numbers
        for r in range(cell_range[0][0], cell_range[1][0] + 1):
            for c in range(cell_range[0][1], cell_range[1][1] + 1):
                cellset.append(self.grid[r][c])
        cellset = set(cellset)

        # fullset minus union of all existion numbers in row, column, cell block
        result = fullset.difference(rowset.union(columnset.union(cellset)))
        return result

    def get_number_block(self, x):
        # get all non zero numbers in a block x(1-8)
        coord = self.cell[x]
        l = []
        for i in range(coord[0][0], coord[1][0] + 1):
            for j in range(coord[0][1], coord[1][1] + 1):
                if self.grid[i][j] != 0:
                    l.append(self.grid[i][j])
        return l

    def get_cell_number(self, x, y):
        # get cell number of any position x,y
        x = x // self.rank
        y = y // self.rank
        return x * 3 + y

    def get_cell_coord(self, x, y):
        # get coords of the cell that position x,y resides in
        return self.cell[self.get_cell_number(x, y)]

    def display(self):
        # standard grid display as numpy array
        print("Grid:")
        print(self.grid)
        print(" Shape: ", self.grid.shape)

    def pretty(self, full=1):
        # prints grid in conventional form
        # full = 0 for minimal and full = 1 (default) for complete grid
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


def numberToBase(n, b):
    if n == 0:
        return [0, 0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    if len(digits) == 1:
        digits.append(0)
    return digits[::-1]


if __name__ == "__main__":
    logging.basicConfig(
        filename="C:/Users/rajatshr/Desktop/Code/Misc/sudoku/app.log",
        filemode="w",
        format=" %(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        level=logging.INFO,
    )
    logging.critical("start")

    a = Sudoku(sourcefile="c:/Users/rajatshr/Desktop/Code/Misc/sudoku/sudoku_input.txt")
    b = Sudoku(sourcefile="c:/Users/rajatshr/Desktop/Code/Misc/sudoku/sudoku_sol.txt")
    a.solve_backtrack()
    a.pretty(0)

