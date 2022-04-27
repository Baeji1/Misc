"""

The problem:

Given an input list of cardinal directions eg. [NORTH,SOUTH,EAST,WEST,WEST] reduce the list to just the relevant direction ie. [WEST]


"""

from typing import List
import logging
from random import randint
from random import choice
from time import time


class Solution:
    def __init__(self):
        self.d = {"N": 0, "S": 0, "E": 0, "W": 0}

    def count(self, directions: List[str]):
        self.d = {"N": 0, "S": 0, "E": 0, "W": 0}
        for x in directions:
            self.d[x] += 1

    def solve(self, directions: List[str]) -> List[str]:
        if not directions:
            return []
        self.count(directions)
        x = self.d["E"] - self.d["W"]
        y = self.d["N"] - self.d["S"]
        dx = ["W", "E"][x > 0]
        dy = ["S", "N"][y > 0]
        return [dx] * abs(x) + [dy] * abs(y)


def cardinal(directions: List[str]) -> (int, int):
    x, y = 0, 0
    dy = {"N": 1, "S": -1}
    dx = {"W": -1, "E": 1}

    for d in directions:
        if d in dx:
            x += dx[d]
        else:
            y += dy[d]

    return (x, y)


def main():
    main_start = time()
    str_len_range = 200
    test_range = 7000

    verify = 0
    t = []
    solver = Solution()
    for i in range(test_range):
        test = "".join(
            [choice(["N", "S", "E", "W"]) for _ in range(randint(0, str_len_range))]
        )
        start = time()
        result = solver.solve(test)
        end = time()
        t.append(end - start)
        # print(f" Input: {test}\n Result: {result}")
        # print(f" Verify: {cardinal(test) == cardinal(result)}\n")
        verify += cardinal(test) == cardinal(result)
        if i % int(test_range * 0.05) == 0:
            print(f"{i/test_range * 100: .2f}%")

    print(f" Total: {test_range}\t Verified: {verify}")
    print(
        f" Total time: {time()-main_start}\t Solve time: {sum(t)}\t Average time: {sum(t)/len(t)}"
    )


if __name__ == "__main__":
    main()
