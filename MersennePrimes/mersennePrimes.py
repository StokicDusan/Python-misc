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


def is_Mersenne(v):
    cand = 2**v-1
    LL = 4
    for i in range(1, v-1):
        if LL > cand:
            if LL % cand == 0:
                return True
            LL = (LL**2-2) % cand
        else:
            LL = LL**2-2
    if LL > cand:
        if LL % cand == 0:
            return True
    elif LL == 0:
        return True
    return False


def mersenne_primes(n: int) -> None:
    value, m = 0, 1
    if n > 0:
        print(3, end=" ")
    while(1):
        if m >= n:
            break
        value += 1
        if is_prime(value):
            if is_Mersenne(value):
                print(2**value-1, end=" ")
                m += 1


def mersenne_primes_format(n: int) -> None:
    value, m = 0, 1
    if n > 0:
        print(m, ': 2**2-1', end="")
        print('-->', 3, "\n")
    while(1):
        if m >= n:
            break
        value += 1
        if is_prime(value):
            if is_Mersenne(value):
                print(m+1, ': 2**{}-1'.format(value), end="")
                print('-->', f'{(2**value)-1:,}', "\n")
                m += 1


def test_mersenne_primes():
    """
    >>> mersenne_primes(0)

    >>> mersenne_primes(1)
    3 
    >>> mersenne_primes(4)
    3 7 31 127 
    >>> mersenne_primes(7)
    3 7 31 127 8191 131071 524287 
    >>> mersenne_primes(-20)

    >>> mersenne_primes_format(4)
    1 : 2**2-1--> 3 
    <BLANKLINE>
    2 : 2**3-1--> 7 
    <BLANKLINE>
    3 : 2**5-1--> 31 
    <BLANKLINE>
    4 : 2**7-1--> 127 
    <BLANKLINE>
    """
    pass


if __name__ == "__main__":
    if(sys.argv[1:]):
        mersenne_primes(int(sys.argv[1]))
    else:
        testmod()
