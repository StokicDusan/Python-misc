# Lucas Sequence L is a sequence of numbers
# such that L(n) = L(n-1) + L(n-2)

from time import perf_counter
from math import sqrt
import sys


class Stopwatch:
    def __init__(self):
        self.reset()

    def start(self):
        if not self.__running:
            self.__start_time = perf_counter()
            self.__running = True
        else:
            print('Stopwatch already running')

    def stop(self):
        if self.__running:
            self.__elapsed += perf_counter()-self.__start_time
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


def print_time(time: float) -> None:
    print('\nElapsed: ', end="")
    if time > 1:
        elapsed = round(time, 3)
        print('%.3f s' % elapsed)
    elif time > 0.001:
        elapsed = time*1000
        elapsed = round(elapsed, 2)
        print('%.2f ms' % elapsed)
    else:
        elapsed = time()*1000000
        elapsed = round(elapsed, 2)
        print('%.2f µs' % elapsed)


def lucas_sequence(n0: int, n1: int, n2: int) -> None:
    L0, L1 = n0, n1
    if n2 >= 1:
        print(L0, end=" ")
    if n2 >= 2:
        print(L1, end=" ")
    for i in range(0, n2-2):
        print(L0+L1, end=" ")
        L0, L1 = L1, L0+L1


def lucas_sequence_timer(n0: int, n1: int, n2: int) -> None:
    timer = Stopwatch()
    timer.start()
    L0, L1 = n0, n1
    if n2 >= 1:
        print(L0, end=" ")
    if n2 >= 2:
        print(L1, end=" ")
    for i in range(0, n2-2):
        print(L0+L1, end=" ")
        L0, L1 = L1, L0+L1
    timer.stop()
    print_time(timer.elapsed)


def lucas_sequence_last(n0: int, n1: int, n2: int) -> None:
    L0, L1 = n0, n1
    for i in range(0, n2-2):
        L0, L1 = L1, L0+L1
    print(L1)


def lucas_sequence_last_timer(n0: int, n1: int, n2: int) -> None:
    timer = Stopwatch()
    timer.start()
    L0, L1 = n0, n1
    for i in range(0, n2-2):
        L0, L1 = L1, L0+L1
    print(L1)
    timer.stop()
    print_time(timer.elapsed)



if __name__ == "__main__":
    if(sys.argv[3:]):
        lucas_sequence(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))