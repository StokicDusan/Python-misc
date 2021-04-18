from math import log2
from cont import Stopwatch
import sys


def TCS(yy):
    global x, p, twin, cousin, sexy, prime, mmm
    x += 1
    if (yy-1)/4 == ((yy-1)/4)//1:
        p += 1
    for r in prime:
        if yy-r == 2:
            twin += 1
        elif yy-r == 4:
            cousin += 1
        elif yy-r == 6:
            sexy += 1
    prime[mmm % 3] = yy
    mmm += 1


def mersenne(yy):
    global m, Mersenne_Primes
    if log2(yy+1) == log2(yy+1)//1:
        trial_factor = 2
        is_Mersenne = True
        while trial_factor < log2(yy+1):
            if log2(yy+1) % trial_factor == 0:
                is_Mersenne = False
                break
            trial_factor += 1
        if is_Mersenne:
            if yy not in Mersenne_Primes:
                Mersenne_Primes += [yy]
                m += 1


def count(pr, max_value):
    global x, m, twin, cousin, sexy, mmm, p
    global prime, Mersenne_Primes, timer
    timer.start()
    nonprimes = max_value * [False]
    nonprimes[0] = nonprimes[1] = True
    if pr == 1:
        for i in range(2, max_value):
            if not nonprimes[i]:
                for j in range(2*i, max_value, i):
                    nonprimes[j] = True
    if pr == 2 or pr == 3:
        for i in range(2, max_value):
            if not nonprimes[i]:
                TCS(i)
                mersenne(i)
                for j in range(2*i, max_value, i):
                    nonprimes[j] = True
    timer.stop()
    if pr == 1 or pr == 3:
        k = 0
        for i in nonprimes:
            if i == False:
                print(k, end=" ")
                k += 1
            else:
                k += 1
    print()
    return max_value


def display(n):
    global x, m, Mersenne_Primes, twin, count, sexy, p, timer
    print('There are', f'{x:,}', 'Primes!!!!')
    print('%.3f' % (x*100/n), '% are Primes', sep="")
    print('There are', f'{m:,}', 'Mersenne Primes { Mp=2**p-1 }', end=": ")
    for i in Mersenne_Primes:
        print(i, end=" ")
    print()
    print('There are', f'{twin:,}', 'Twin Primes')
    print('There are', f'{cousin:,}', 'Cousin Primes')
    print('There are', f'{sexy:,}', 'Sexy Primes')
    print('There are', f'{p:,}', 'Pythagorean Primes { Pp=4n+1 }', end="")
    print()
    print('Elapsed:', round(timer.elapsed(), 6), 'seconds')


def main(argv1, argv2):
    n = count(int(argv1), int(argv2)+1)
    if int(argv1) == 2 or int(argv1) == 3:
        display(n)
    print()


x, m, twin, cousin, sexy, mmm, p = 0, 0, 0, 0, 0, 0, 0
prime = [3, 5, 7]
Mersenne_Primes = []
if __name__ == "__main__":
    timer = Stopwatch()
    main(sys.argv[1], sys.argv[2])
    print()
