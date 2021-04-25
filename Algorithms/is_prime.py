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


def test_is_prime() -> None:
    """
    >>> is_prime(1)
    False
    >>> is_prime(40)
    False
    >>> is_prime(165)
    False
    >>> is_prime(701)
    True
    >>> is_prime(2187)
    False
    """
    pass


if __name__ == "__main__":
    from doctest import testmod
    testmod()
