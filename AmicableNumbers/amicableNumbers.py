# Prints out pairs of amicable numbers
# where the smaller in the pair is
# lower or equal then the entered number

from math import sqrt
from time import clock
from doctest import testmod


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


def sum_of_divisors(n):
    """
    Returns the sum of all
    true divisors (and 1)
    for n > 1
    """
    if is_prime(n):
        return 1
    i = n-1
    SumOfDivisors = 0
    while i:
        if n % i == 0:
            SumOfDivisors += i
        i -= 1
    return SumOfDivisors


def is_prime(pp):
    """
    Returns True if pp is prime
    otherwise, returns False
    Note: not a very sophisticated check
    """
    if pp == 1:
        return False
    trial = 2
    root = sqrt(pp)
    while trial <= root:
        if is_prime(trial):
            if pp % trial == 0:
                return False
        trial += 1
    return True


def amicable_numbers(k: int):
    """
    >>> amicable_numbers(300)
    [ 220  ,  284 ]
    >>> amicable_numbers(3000)
    [ 220  ,  284 ]
    [ 1184  ,  1210 ]
    [ 2620  ,  2924 ]
    >>> amicable_numbers(5020)
    [ 220  ,  284 ]
    [ 1184  ,  1210 ]
    [ 2620  ,  2924 ]
    [ 5020  ,  5564 ]
    >>> amicable_numbers("some text")
    Traceback (most recent call last):
        ...
    TypeError: amicable_numbers accepts only integer arguments.
    """
    if not isinstance(k, int):
        raise TypeError("amicable_numbers accepts only integer arguments.")
    L = [1, 2]
    for i in range(1, (1+k)):
        j = sum_of_divisors(i)
        if i not in L and j != i:
            if sum_of_divisors(j) == i:
                L += [j]
                print('[', i, ' , ', j, ']')


def amicable_numbers_time(k: int):
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


timer = Stopwatch()

if __name__ == "__main__":
    testmod()
    k = eval(input('Search for Amicable numbers up to:\n').strip())
    print('Prints out pairs of amicable numbers without time elapsed:')
    amicable_numbers(k)
