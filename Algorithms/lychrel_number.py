def lychrel(n: int):
    """
    A test for lychrel numbers
    candidates in base 10
    capping at 10,000 
    """
    cap, i, numb = 10000, 0, n
    while i < cap:
        if numb == int(str(numb)[::-1]):
            return i
        else:
            numb = numb+int(str(numb)[::-1])
        i += 1
    return True


def test_lychrel():
    """
    >>> lychrel(1)
    0
    >>> lychrel(40)
    1
    >>> lychrel(119)
    2
    >>> lychrel(196)
    True
    """
    pass


if __name__ == "__main__":
    from doctest import testmod
    testmod()
