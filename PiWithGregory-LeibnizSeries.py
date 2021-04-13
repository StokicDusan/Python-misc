# Gregory-Leibniz Series converges to pi very slowly.
# You approximately need 10**(c+1) long series for
# a precision up to the c-th decimal digit.

# Based on https://crypto.stanford.edu/pbc/notes/pi/glseries.html

c = eval(input('Pi correct up to what decimal?'))
n = 10**(c+1)
pi = 0
i = 0
k = 0
if c > 6:
    print('This might take awhile....')
while n > k:
    i %= 2
    pi = pi+((-1)**i)*(4/(2*k+1))
    i += 1
    k += 1
    pi = round(pi, c+3)
print(((pi*(10**c))//1)/(10**c))
