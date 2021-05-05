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


def is_palindromic_number(numb: int) -> bool:
    return numb == int(str(numb)[::-1])


def is_emirp(n) -> bool:
    """
    Returns whether or not n
    is an emirp number.
    Emirps are primes whose reversal is a different prime
    https://oeis.org/A006567
    """
    if not is_prime(n):
        return False
    if not is_palindromic_number(n):
        return is_prime(int(str(n)[::-1]))
    else:
        return False


def print_emirp(x: int) -> None:
    for i in range(1, x+1):
        if is_emirp(i):
            print(i, end=" ")


def print_emirp_count(x: int) -> None:
    xx = 0
    for i in range(1, x+1):
        if is_emirp(i):
            xx += 1
            print(i, end=" ")
    print()
    print('There where ', f'{xx:,}', ' emirps')


def test_print_emirp():
    """
    >>> print_emirp(0)

    >>> print_emirp(10)

    >>> print_emirp(100)
    13 17 31 37 71 73 79 97 
    >>> print_emirp(311)
    13 17 31 37 71 73 79 97 107 113 149 157 167 179 199 311 
    >>> print_emirp(-500)

    >>> print_emirp_count(10)
    <BLANKLINE>
    There where  0  emirps
    >>> print_emirp_count(100)
    13 17 31 37 71 73 79 97 
    There where  8  emirps
    >>> print_emirp_count(311)
    13 17 31 37 71 73 79 97 107 113 149 157 167 179 199 311 
    There where  16  emirps
    """
    pass


if __name__ == "__main__":
    if(sys.argv[1:]):
        print_emirp(int(sys.argv[1]))
    else:
        testmod()
