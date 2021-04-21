from math import log2


def rev(A):
    for i in range(0, len(A)):
        A[i] = -A[i]
    return A


def fajl(K):
    f = open("vols.txt", "w+")
    for i in range(0, len(K)):
        for j in range(0, len(K[i])):
            f.write('C_'+str(len(K[i]))+','+str(j)+str(K[i][j])+'\n')
        f.write('\n')
    print('Done!')
    f.close()


def ispis(K):
    print()
    for i in range(0, len(K)):
        for j in range(0, len(K[i])):
            print('C_'+str(len(K[i]))+','+str(j), end='=')
            print(K[i][j])
        print()


def stablo(A):
    global kod
    for i in range(0, A+1):
        kod.append([])
    kod[0].append([1])
    for i in range(1, A+1):
        for j in range(0, len(kod[i-1])):
            kod[i].append(kod[i-1][j][:int((2**i)/2)] +
                          list(kod[i-1][j][:int((2**i)/2)]))
            kod[i].append(kod[i-1][j][:int((2**i)/2)] +
                          list(rev(kod[i-1][j][:int((2**i)/2)])))


def main():
    global kod
    while 1:
        nn = int(input('1.Print OVSF codes\n2.Save codes in file\n'))
        if(nn == 1 or nn == 2):
            break
    while 1:
        n = int(input('SF='))
        if((n & (n-1) == 0) and n != 0):
            break
    stablo(int(log2(n)))
    if (nn == 1):
        ispis(kod)
    elif (nn == 2):
        fajl(kod)


kod = []
main()
