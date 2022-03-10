import os
import logging


def markdiag(x: List[List[str]], c: int, j: int):
    n = len(x[0])
    return n


def checkdiag(n: int):
    x = [["." for i in range(n)] for j in range(n)]

    c = n // 2

    for j in range(n):
        markdiag(x, c, j)

    print(x)


def main():
    path = os.getcwd()

    logging.basicConfig(
        filename=os.path.join(path, "nqueens/app.log"),
        filemode="w",
        format=" %(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        level=logging.WARNING,
    )
    logging.critical("start")


if __name__ == "__main__":
    main()
