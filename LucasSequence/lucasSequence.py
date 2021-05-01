# Lucas Sequence L is a sequence of numbers
# such that L(n) = L(n-1) + L(n-2)

from time import perf_counter

class Stopwatch:
    def __init__(self):
        self.reset()

    def start(self):
        if not self.__running:
            self.__start_time = perf_counter()
            self.__running = True
        else:
            print('Stopwatch already running')

    def stop(self):
        if self.__running:
            self.__elapsed += perf_counter()-self.__start_time
            self.__running = False
        else:
            print('Stopwatch not running')

    def reset(self):
        self.__start_time = self.__elapsed = 0
        self.__running = False

    def elapsed(self):
        if not self.__running:
            return self.__elapsed
        else:
            print('Stopwatch must be stopped')
            return None


def Continue(n):
    while(1):
        x=str(input('continue?(Y\\N) :'))
        if x.upper()=="N":
            return 0
        elif x.upper()=="Y":
            print()
            return 1


def main():
    timer = Stopwatch()
    while 1:
        k = int(eval(input('Display:\n1.Last number\n2.Entire sequence\n')))
        if k == 1 or k == 2:
            break
    L0, L1 = eval(input('Enter the first two values for the sequence:'))
    n = eval(input('Enter the Length of the sequence:'))
    timer.start()
    if k == 1:
        n = n+1
        for i in range(0, n-3):
            L0,L1 = L1,L0+L1
    if k == 2:
        print(L0, end=" ")
        print(L1, end=" ")
        print(L0+L1, end=" ")
        for i in range(0, n-3):
            L0,L1 = L1,L0+L1
            print(L0+L1, end=" ")
    timer.stop()
    print()
    if k == 1:
        print(L1)
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
