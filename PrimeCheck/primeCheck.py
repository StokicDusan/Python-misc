from math import sqrt
import sys


def factors(A, x):
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


def all_prime_factors(p):
    factors = []
    loop = 2
    while loop * loop <= p:
        if p % loop == 0:
            p //= loop
            factors.append(loop)
        else:
            loop += 1
#        print('Searching(%.5f%%)' % (100*loop/p), end="\r")
    factors.sort()
    print('                           ', end="\r")
    return factors


def is_prime(pp):
    global com
    if pp == 1:
        return False
    trial = 2
    root = sqrt(pp)
    while trial <= root:
#        print('Searching(%.5f%%)' % (100*trial/root), end="\r")
        if pp % trial == 0:
            print('This number is not prime')
            com = all_prime_factors(pp)
            return False
        trial += 1
    return True


def main(argv):
    global com
    x = int(argv)
    if is_prime(x):
        print('This number is Prime!!!')
    else:
        factors(com, x)


com = []
if __name__ == "__main__":
    main(sys.argv[1])
