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


def Continue(n):
    while(1):
        x = str(input('continue?(Y\\N) :'))
        if x.upper() == "N":
            return 0
        elif x.upper() == "Y":
            print()
            return 1


def main():
    x = eval(input('Display emirp up to what value?'))
    xx = 0
    for i in range(1, x):
        if is_emirp(i):
            xx += 1
            print(i, end=" ")
    print()
    print('There where ', f'{xx:,}', ' emirps')


c = 1
while c:
    if __name__ == "__main__":
        main()
        c = Continue(c)
