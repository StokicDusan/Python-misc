# Lucas numbers are numbers of the Lucas Sequence
# where L(n) = L(n-1) + L(n-2), L(0) = 2 and L(1) = 1
# https://oeis.org/A000032

from doctest import testmod
import sys


def lucas_numbers(limit: int) -> None:
    Lucas1, Lucas2 = 2, 1
    if limit >= 1:
        print(Lucas1, end=" ")
    if limit >= 2:
        print(Lucas2, end=" ")
    for i in range(0, limit-2):
        print(Lucas1+Lucas2, end=" ")
        Lucas1, Lucas2 = Lucas2, Lucas1+Lucas2


def lucas_numbers_last(limit: int) -> None:
    Lucas1, Lucas2 = 2, 1
    for i in range(0, limit-2):
        Lucas1, Lucas2 = Lucas2, Lucas1+Lucas2
    print(Lucas2)


def test_lucas_numbers():
    """
    >>> lucas_numbers(0)

    >>> lucas_numbers(1)
    2 
    >>> lucas_numbers(3)
    2 1 3 
    >>> lucas_numbers(7)
    2 1 3 4 7 11 18 
    >>> lucas_numbers(-20)

    >>> lucas_numbers_last(3)
    3
    >>> lucas_numbers_last(15)
    843
    >>> lucas_numbers_last(45)
    1568397607
    """
    pass


if __name__ == "__main__":
    if(sys.argv[1:]):
        lucas_numbers(int(sys.argv[1]))
    else:
        testmod()
