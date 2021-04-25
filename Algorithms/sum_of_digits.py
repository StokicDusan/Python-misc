def sum_of_digits(number: int) -> int:
    """
    Returns the sum of digits
    for the entered number 
    """
    return eval("+".join([i for i in str(number)]))


def test_sum_of_digits() -> None:
    """
    >>> sum_of_digits(1)
    1
    >>> sum_of_digits(40)
    4
    >>> sum_of_digits(165)
    12
    >>> sum_of_digits(701)
    8
    >>> sum_of_digits(2187)
    18
    """
    pass


if __name__ == "__main__":
    from doctest import testmod
    testmod()
