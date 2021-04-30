# Lucas numbers are numbers of the Lucas Sequence
# where L(n) = L(n-1) + L(n-2), L(0) = 2 and L(1) = 1
# https://oeis.org/A000032

limit = int(input('Display first ? Lucas numbers:'))
Lucas = [2, 1]
Lucas1=2
Lucas2=1
print(Lucas1, end=" ")
print(Lucas2, end=" ")
for i in range(0, limit-2):
    print(Lucas1+Lucas2, end=" ")
    Lucas1,Lucas2 =Lucas2, Lucas1+Lucas2

