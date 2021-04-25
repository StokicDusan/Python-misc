from math import sqrt


def is_prime(pp: int) -> bool:
    """
    Returns True if pp is prime
    otherwise, returns False
    Note: not a very sophisticated check
    """
    if pp == 2 or pp == 3:
        return True
    elif pp < 2 or not pp % 2:
        return False

    odd_n = range(3, int(sqrt(pp) + 1), 2)
    return not any(not pp % i for i in odd_n)


def sum_of_divisors(n: int) -> int:
    """
    Returns the sum of all
    non-trivial divisors
    for n > 1
    """
    if is_prime(n):
        return 0
    i = n-1
    SumOfDivisors = 0
    while i:
        if n % i == 0:
            SumOfDivisors += i
        i -= 1
    return SumOfDivisors


def test_sum_of_divisors() -> None:
    """
    >>> sum_of_divisors(1)
    0
    >>> sum_of_divisors(210)
    366
    >>> sum_of_divisors(311)
    0
    >>> sum_of_divisors(1024)
    1023
    """
    pass


if __name__ == "__main__":
    from doctest import testmod
    testmod()
