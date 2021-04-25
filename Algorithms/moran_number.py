from math import sqrt


def is_prime(pp) -> bool:
    """
    Returns True if pp is prime
    otherwise, returns False
    """
    if pp == 2 or pp == 3:
        return True
    elif pp < 2 or not pp % 2:
        return False

    odd_n = range(3, int(sqrt(pp) + 1), 2)
    return not any(not pp % i for i in odd_n)


def moran_number(n: int) -> str:
    """
    Returns if a number is Moran, Harshad or neither.
    Moran numbers are a subset of Harshad numbers.
    Moran numbers https://oeis.org/A001101
    Harshad numbers https://oeis.org/A005349
    """
    num = eval("+".join([i for i in str(n)]))
    if n % num == 0:
        if is_prime(n/num):
            return "Moran"
        else:
            return "Harshad"
    else:
        return "Neither"


def test_moran_number() -> None:
    """
    >>> moran_number(1)
    'Harshad'
    >>> moran_number(40)
    'Harshad'
    >>> moran_number(111)
    'Moran'
    >>> moran_number(701)
    'Neither'
    >>> moran_number(2187)
    'Neither'
    """
    pass


if __name__ == "__main__":
    from doctest import testmod
    testmod()
