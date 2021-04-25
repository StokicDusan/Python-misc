from math import sqrt


def is_prime_simple(pp: int) -> bool:
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
        if is_prime_simple(trial):
            if pp % trial == 0:
                return False
        trial += 1
    return True


def test_is_prime_simple() -> None:
    """
    >>> is_prime_simple(1)
    False
    >>> is_prime_simple(40)
    False
    >>> is_prime_simple(165)
    False
    >>> is_prime_simple(701)
    True
    >>> is_prime_simple(2187)
    False
    """
    pass


if __name__ == "__main__":
    from doctest import testmod
    testmod()
