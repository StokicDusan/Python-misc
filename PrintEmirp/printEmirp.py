from func import is_emirp
import cont


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
        c = cont.Continue(c)
