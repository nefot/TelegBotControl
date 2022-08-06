# from time import sleep, time
#
# path = "Logs/"
# sec = 1  # секунды
#
#
# def main():
#     while True:
#         sleep(sec)
import logging


module_logger = logging.getLogger("exampleApp.otherMod2")


def add(x, y):
    """"""
    logger = logging.getLogger("exampleApp.otherMod2.add")
    logger.info("added %s and %s to get %s" % (x, y, x + y))
    return x + y
def main():
    """
    The main entry point of the application
    """

    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("new_snake.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    result = add(7, 8)
    logger.info("Done!")


if __name__ == "__main__":
    main()