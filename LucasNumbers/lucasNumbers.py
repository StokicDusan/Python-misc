# Lucas numbers are numbers of the Lucas Sequence
# where L(n) = L(n-1) + L(n-2), L(0) = 2 and L(1) = 1
# https://oeis.org/A000032

limit = int(input('Display first ? Lucas numbers:'))
Lucas = [2, 1]
for i in Lucas:
    print(i, end=" ")
for i in range(0, limit-2):
    print(Lucas[0]+Lucas[1], end=" ")
    Lucas[i % 2] = Lucas[0]+Lucas[1]
