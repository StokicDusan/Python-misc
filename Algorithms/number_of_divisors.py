def number_of_divisors(n) -> int:
    """
    Returns the number of all 
    non-trivial divisors
    """
    n = abs(n)
    i = 2
    NumberOfDivisors = 0
    while i < n:
        if n % i == 0:
            NumberOfDivisors += 1
        i += 1
    return NumberOfDivisors


def test_number_of_divisors() -> None:
    """
    >>> number_of_divisors(1)
    0
    >>> number_of_divisors(210)
    14
    >>> number_of_divisors(311)
    0
    >>> number_of_divisors(1024)
    9
    """
    pass


if __name__ == "__main__":
    from doctest import testmod
    testmod()
