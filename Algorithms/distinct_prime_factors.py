def distinct_prime_factors(x: int) -> list:
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


def test_distinct_prime_factors() -> None:
    """
    >>> distinct_prime_factors(1)
    []
    >>> distinct_prime_factors(40)
    [2, 5]
    >>> distinct_prime_factors(165)
    [3, 5, 11]
    >>> distinct_prime_factors(701)
    [701]
    >>> distinct_prime_factors(2187)
    [3]
    """
    pass


if __name__ == "__main__":
    from doctest import testmod
    testmod()
