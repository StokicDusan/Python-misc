from math import sqrt
import sys


def factors(A: list, x: int) -> None:
    print('%i = ' % x, end="")
    k, i = 0, 0
    while i < len(A):
        n = A.count(A[i])
        if n == 1:
            print(f'{A[i]:,}', end="")
            k += 1
            i += 1
        else:
            print('{}^{}'.format(f'{A[i]}', n), end="")
            s = A[i]
            while s in A:
                A.remove(s)
        if k < len(A):
            print(' * ', end="")
    print()


def all_prime_factors(p: int) -> list:
    number = p
    allFactors = []
    loop = 2
    while loop * loop <= p:
        if p % loop == 0:
            p //= loop
            allFactors.append(loop)
        else:
            loop += 1
    if p > 1:
        allFactors.append(p)
    allFactors.sort()
    factors(allFactors, number)


def is_prime(pp: int) -> bool:
    if pp == 2 or pp == 3:
        return True
    elif pp < 2 or not pp % 2:
        return False

    odd_n = range(3, int(sqrt(pp) + 1), 2)
    return not any(not pp % i for i in odd_n)


def main(argv):
    x = int(argv)
    if is_prime(x):
        print('This number is Prime!!!')
    else:
        all_prime_factors(x)


if __name__ == "__main__":
    main(sys.argv[1])
