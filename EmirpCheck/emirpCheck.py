# Checks if the entered integer is an Emirp number or not.

# An emirp is a prime number that results in a
# different prime when its decimal digits are reversed.

from func import is_palindromic_number, is_emirp
import sys


def main(argv):
    x = int(argv)
    if not is_palindromic_number(x):
        if is_emirp(x):
            print('It is an Emirp!')
        else:
            print('It is not an Emirp')
    else:
        print('It is not an Emirp, palindromes don\'t count\n')


if __name__ == "__main__":
    main(sys.argv[1])
