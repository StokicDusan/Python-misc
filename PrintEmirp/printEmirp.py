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



if __name__ == "__main__":
    if(sys.argv[1:]):
        print_emirp(int(sys.argv[1]))

