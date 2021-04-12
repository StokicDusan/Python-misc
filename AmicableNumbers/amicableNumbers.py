# Prints out pairs of amicable numbers
# lower then the entered number

from math import sqrt
from cont import Continue, Stopwatch


def sum_of_divisors(n):
    """
    Returns the sum of all
    true divisors (and 1)
    for n > 1
    """
    if is_prime(n):
        return 1
    i = n-1
    SumOfDivisors = 0
    while i:
        if n % i == 0:
            SumOfDivisors += i
        i -= 1
    return SumOfDivisors


def is_prime(pp):
    """
    Returns True if pp is prime
    otherwise, returns False
    Note: not a very sophisticated check
    """
    if pp == 1:
        return False
    trial = 2
    root = sqrt(pp)
    while trial <= root:
        if is_prime(trial):
            if pp % trial == 0:
                return False
        trial += 1
    return True


def main():
    k = int(input('Search for Amicable numbers up to '))
    timer.start()
    L = [1, 2]
    for i in range(1, (1+k)):
        j = sum_of_divisors(i)
        if i not in L and j != i:
            if sum_of_divisors(j) == i:
                L += [j]
                print('[', i, ' , ', j, ']  ')
#        print('Searching(%.2f%%)'%(i*100/k),end="\r")
    timer.stop()
    print('Done!                 ', end='\r')
    print('\ntime elapsed: %.4f s' % round(timer.elapsed(), 4))


timer = Stopwatch()
if __name__ == "__main__":
    main()
    timer.reset()
    print()
