from math import sqrt
from math import fabs
from decimal import Decimal
from time import clock


def all_prime_factors(p):
    """
    Returns a list of distinct
    prime factors of the number x
    """
    factors = []
    loop = 2
    while loop <= p:
        if p % loop == 0:
            p //= loop
            factors.append(loop)
        else:
            loop += 1
    return factors


def DistinctPrimeFactors(x):
    factors = []
    """
    Returns a list of distinct
    prime factors of the number x
    """
    loop = 2
    while loop <= x:
        if x % loop == 0:
            while x//loop == x/loop:
                x //= loop
            factors.append(loop)
        else:
            loop += 1
    return factors


def moran(n):
    """
    Returns if a number is Moran, Harshad or neither
    Morad numbers https://oeis.org/A001101
    Harshad numbers https://oeis.org/A005349
    """
    num = 0
    for i in str(n):
        num += int(i)
    if n % num == 0:
        if is_prime(n/num):
            return "Moran"
        else:
            return "Harshad"
    else:
        return "Neither"


def lychrel(n):
    """
    A test for lychrel numbers
    https://oeis.org/A306481
    """
    cap, i, numb = 10000, 0, n
    while i < cap:
        if numb == int(str(numb)[::-1]):
            return i
        else:
            numb = numb+int(str(numb)[::-1])
        i += 1
    return True


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


def is_palindromic_number(numb):
    """
    Returns whether on not numb
    is a palindromic number
    https://oeis.org/A002113
    """
    return numb == reverse_digit_order(numb)


def SOD(number):
    """
    Returns the sum of digits
    for the entered number 
    """
    return eval("+".join([i for i in str(number)]))


def is_triangular(s):
    """
    Returns True if s is a triangular
    number: can be written as (s+1)*s/2
    https://oeis.org/A000217
    """
    t = 0
    i = 0
    while t < s:
        i += 1
        t += i
    if t == s:
        return True
    return False


def reverse_digit_order(n):
    """
    Returns the entered number with
    reversed digits
    i.e. for n=1205 returns 5021
         for n=-123 returns -321
    """
    if n > 0:
        return float(str(n)[::-1])
    return -float(str(int(fabs(n)))[::-1])


def is_emirp(n):
    """
    Returns whether or not n
    is an emirp number.
    Emirps are primes whose reversal is a different prime
    https://oeis.org/A006567
    """
    if not is_prime(n):
        return False
    if not is_palindromic_number(n):
        return is_prime(reverse_digit_order(n))
    else:
        return False


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


def number_of_divisors(n):
    """
    Returns the number of all 
    true divisors (and 1)
    """
    n = abs(n)
    i = 1
    NumberOfDivisors = 0
    while i <= n:
        if n % i == 0:
            NumberOfDivisors += 1
        i += 1
    return NumberOfDivisors
