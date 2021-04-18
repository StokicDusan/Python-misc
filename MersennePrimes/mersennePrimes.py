from func import is_prime


def is_Mersenne(v):
    cand = 2**v-1
    LL = 4
    for i in range(1, v-1):
        if LL > cand:
            if LL % cand == 0:
                return True
            LL = (LL**2-2) % cand
        else:
            LL = LL**2-2
    if LL > cand:
        if LL % cand == 0:
            return True
    elif LL == 0:
        return True
    return False


def main():
    max_value = eval(input('display how many Mersenne primes?'))
    value, m = 0, 0
    while(1):
        if m >= max_value:
            break
        value += 1
        if m == 0:
            print(m+1, ': 2**2-1', end="")
            print('-->', 3, "\n")
            m += 1
        if is_prime(value):
            if is_Mersenne(value):
                print(m+1, ': 2**{}-1'.format(value), end="")
                print('-->', f'{(2**value)-1:,}', "\n")
                m += 1

    print()


if __name__ == "__main__":
    main()
