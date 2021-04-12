from math import sqrt
from math import fabs
from decimal import Decimal
from time import clock


def Continue(n):
    while(1):
        x = str(input('continue?(Y\\N) :'))
        if x.upper() == "N":
            return 0
        elif x.upper() == "Y":
            print()
            return 1


class Stopwatch:
    def __init__(self):
        self.reset()

    def start(self):
        if not self.__running:
            self.__start_time = clock()
            self.__running = True
        else:
            print('Stopwatch already running')

    def stop(self):
        if self.__running:
            self.__elapsed += clock()-self.__start_time
            self.__running = False
        else:
            print('Stopwatch not running')

    def reset(self):
        self.__start_time = self.__elapsed = 0
        self.__running = False

    def elapsed(self):
        if not self.__running:
            return self.__elapsed
        else:
            print('Stopwatch must be stopped')
            return None
