# Prints out pairs of amicable numbers
# where the smaller in the pair is
# lower or equal then the entered number

from math import sqrt
from time import perf_counter
from doctest import testmod
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


def is_prime(pp: int) -> bool:
    if pp == 2 or pp == 3:
        return True
    elif pp < 2 or not pp % 2:
        return False

    odd_n = range(3, int(sqrt(pp) + 1), 2)
    return not any(not pp % i for i in odd_n)


def sum_of_divisors(n: int) -> int:
    if is_prime(n):
        return 1
    i = n-1
    SumOfDivisors = 0
    while i:
        if n % i == 0:
            SumOfDivisors += i
        i -= 1
    return SumOfDivisors

def amicable_numbers(k: int) -> None:
    if not isinstance(k, int):
        raise TypeError("amicable_numbers accepts only integer arguments.")
    L = [1, 2]
    for i in range(1, (1+k)):
        j = sum_of_divisors(i)
        if i not in L and j != i:
            if sum_of_divisors(j) == i:
                L += [j]
                print('[', i, ' , ', j, ']')


def amicable_numbers_time(k: int) -> None:
    if not isinstance(k, int):
        raise TypeError("amicable_numbers accepts only integer arguments.")
    timer.start()
    L = [1, 2]
    for i in range(1, (1+k)):
        j = sum_of_divisors(i)
        if i not in L and j != i:
            if sum_of_divisors(j) == i:
                L += [j]
                print('[', i, ' , ', j, ']')
    timer.stop()
    print('Done!                 ', end='\r')
    print('\ntime elapsed: %.4f s' % round(timer.elapsed(), 4))
    timer.reset()

def test_amicable_numbers():
    """
    >>> amicable_numbers(300)
    [ 220  ,  284 ]
    >>> amicable_numbers(2620)
    [ 220  ,  284 ]
    [ 1184  ,  1210 ]
    [ 2620  ,  2924 ]
    >>> amicable_numbers(3000)
    [ 220  ,  284 ]
    [ 1184  ,  1210 ]
    [ 2620  ,  2924 ]
    >>> amicable_numbers("some text")
    Traceback (most recent call last):
        ...
    TypeError: amicable_numbers accepts only integer arguments.
    """
    pass

timer = Stopwatch()

if __name__ == "__main__":
    if(sys.argv[1:]):
        amicable_numbers(int(sys.argv[1]))
    else:
        testmod()
