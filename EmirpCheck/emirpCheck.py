# Checks if the entered integer is an Emirp number or not.

# An emirp is a prime number that results in a
# different prime when its decimal digits are reversed.

from math import sqrt
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


def main(argv):
    x = int(argv)
    if not is_palindromic_number(x):
        if is_emirp(x):
            print('It is an Emirp!')
        else:
            print('It is not an Emirp')
    else:
        print('It is not an Emirp, palindromes don\'t count\n')


if __name__ == "__main__":
    main(sys.argv[1])
