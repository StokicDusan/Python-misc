def all_prime_factors(p: int) -> list:
    """
    Returns a list of distinct
    prime factors of the number p
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


def test_all_prime_factors() -> None:
    """
    >>> all_prime_factors(1)
    []
    >>> all_prime_factors(40)
    [2, 2, 2, 5]
    >>> all_prime_factors(165)
    [3, 5, 11]
    >>> all_prime_factors(701)
    [701]
    >>> all_prime_factors(2187)
    [3, 3, 3, 3, 3, 3, 3]
    """
    pass


if __name__ == "__main__":
    from doctest import testmod
    testmod()
