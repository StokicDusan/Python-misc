# Euclid numbers are integers of the form En = pn# + 1,
# where pn# is the nth primordial,
# i.e. the product of the first n prime numbers.
# https://oeis.org/A006862

from math import sqrt
from doctest import testmod
import sys


def is_prime(pp: int) -> bool:
    if pp == 2 or pp == 3:
        return True
    elif pp < 2 or not pp % 2:
        return False
    odd_n = range(3, int(sqrt(pp) + 1), 2)
    return not any(not pp % i for i in odd_n)


def euclid_numbers(n: int) -> None:
    value, primorial, k = 1, 1, 0
    while (k <= n):
        if is_prime(value):
            k += 1
            primorial *= value
            print(primorial + 1, end=" ")
        value += 1


def test_euclid_numbers():
    """
    >>> euclid_numbers(0)
    3 
    >>> euclid_numbers(1)
    3 7 
    >>> euclid_numbers(3)
    3 7 31 211 
    >>> euclid_numbers(7)
    3 7 31 211 2311 30031 510511 9699691 
    >>> euclid_numbers(-20)

    """
    pass


if __name__ == "__main__":
    if(sys.argv[1:]):
        euclid_numbers(int(sys.argv[1]))
    else:
        testmod(name="test_euclid_numbers",verbose=True)
