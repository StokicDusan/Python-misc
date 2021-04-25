def is_triangular(number: int) -> bool:
    """
    Returns True if number is a triangular number: 
    can be written as (s+1)*s/2
    https://oeis.org/A000217
    """
    t = 0
    i = 0
    while t < number:
        i += 1
        t += i
    if t == number:
        return True
    return False


def test_is_triangular() -> None:
    """
    >>> is_triangular(1)
    True
    >>> is_triangular(40)
    False
    >>> is_triangular(165)
    False
    >>> is_triangular(630)
    True
    >>> is_triangular(2001000)
    True
    """
    pass


if __name__ == "__main__":
    from doctest import testmod
    testmod()
