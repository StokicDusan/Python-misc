# Lucas Sequence L is a sequence of numbers
# such that L(n) = L(n-1) + L(n-2)

from cont import Stopwatch, Continue


def main():
    timer = Stopwatch()
    while 1:
        k = int(eval(input('Display:\n1.Last number\n2.Entire sequence\n')))
        if k == 1 or k == 2:
            break
    L0, L1 = eval(input('Enter the first two values for the sequence:'))
    L = [L0, L1]
    n = eval(input('Enter the Length of the sequence:'))
    timer.start()
    if k == 1:
        n = n+1
        for i in range(0, n-3):
            L[i % 2] = L[0]+L[1]
    if k == 2:
        for i in L:
            print(i, end=" ")
        print(L[0]+L[1], end=" ")
        for i in range(0, n-3):
            L[i % 2] = L[0]+L[1]
            print(L[0]+L[1], end=" ")
    timer.stop()
    print()
    if k == 1:
        print(L[n % 2])
#        print("The number has ",f'{len(str(L[n % 2])):,}'," digits")
    print('\nElapsed: ', end="")
    if timer.elapsed() > 1:
        elapsed = round(timer.elapsed(), 3)
        print('%.3f s' % elapsed)
    elif timer.elapsed() > 0.001:
        elapsed = timer.elapsed()*1000
        elapsed = round(elapsed, 2)
        print('%.2f ms' % elapsed)
    else:
        elapsed = timer.elapsed()*1000000
        elapsed = round(elapsed, 2)
        print('%.2f µs' % elapsed)


c = 1
while c:
    if __name__ == "__main__":
        main()
        c = Continue(c)
        print()
