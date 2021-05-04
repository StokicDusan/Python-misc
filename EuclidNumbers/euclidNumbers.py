# Euclid numbers are integers of the form En = pn# + 1,
# where pn# is the nth primorial,
# i.e. the product of the first n prime numbers.
# https://oeis.org/A006862

from math import sqrt
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



if __name__ == "__main__":
    if(sys.argv[1:]):
        euclid_numbers(int(sys.argv[1]))
