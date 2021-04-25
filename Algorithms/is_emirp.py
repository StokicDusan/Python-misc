from math import sqrt


def is_prime(pp: int) -> bool:
    if pp == 2 or pp == 3:
        return True
    elif pp < 2 or not pp % 2:
        return False

    odd_n = range(3, int(sqrt(pp) + 1), 2)
    return not any(not pp % i for i in odd_n)


def is_palindromic_number(numb: int) -> bool:
    return numb == int(str(numb)[::-1])


def is_emirp(n) -> bool:
    """
    Returns whether or not n
    is an emirp number.
    Emirps are primes whose reversal is a different prime
    https://oeis.org/A006567
    """
    if not is_prime(n):
        return False
    if not is_palindromic_number(n):
        return is_prime(int(str(n)[::-1]))
    else:
        return False


def test_is_emirp() -> None:
    """
    >>> is_emirp(1)
    False
    >>> is_emirp(165)
    False
    >>> is_emirp(311)
    True
    >>> is_emirp(3221)
    True
    >>> is_emirp(14741)
    False
    """
    pass


if __name__ == "__main__":
    from doctest import testmod
    testmod()
