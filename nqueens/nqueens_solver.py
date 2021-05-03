import os
import logging


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
