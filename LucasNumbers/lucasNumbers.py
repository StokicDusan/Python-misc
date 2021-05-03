# Lucas numbers are numbers of the Lucas Sequence
# where L(n) = L(n-1) + L(n-2), L(0) = 2 and L(1) = 1
# https://oeis.org/A000032


import sys


def lucas_numbers(limit: int) -> None:
    Lucas1, Lucas2 = 2, 1
    if limit >= 1:
        print(Lucas1, end=" ")
    if limit >= 2:
        print(Lucas2, end=" ")
    for i in range(0, limit-2):
        print(Lucas1+Lucas2, end=" ")
        Lucas1, Lucas2 = Lucas2, Lucas1+Lucas2


def lucas_numbers_last(limit: int) -> None:
    Lucas1, Lucas2 = 2, 1
    for i in range(0, limit-2):
        Lucas1, Lucas2 = Lucas2, Lucas1+Lucas2
    print(Lucas2)



if __name__ == "__main__":
    if(sys.argv[1:]):
        lucas_numbers(int(sys.argv[1]))

