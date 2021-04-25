def is_palindromic_number(numb: int) -> bool:
    """
    Returns whether on not numb
    is a palindromic number
    https://oeis.org/A002113
    """
    return numb == int(str(numb)[::-1])


def test_is_palindromic_number() -> None:
    """
    >>> is_palindromic_number(7)
    True
    >>> is_palindromic_number(40)
    False
    >>> is_palindromic_number(484)
    True
    >>> is_palindromic_number(123321)
    True
    """
    pass


if __name__ == "__main__":
    from sys import argv
    if (argv[1:]):
        print(is_palindromic_number(int(argv[1])))
    else:
        from doctest import testmod
        testmod()
