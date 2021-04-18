n = eval(input('Display how many Euclid numbers? '))
value = 1
primorial = 1
k = 0
# Euclid numbers are integers of the form En = pn# + 1,
# where pn# is the nth primorial,
# i.e. the product of the first n prime numbers.
# https://oeis.org/A006862

while 1:
    is_prime = True
    trial_factor = 2
    while is_prime and trial_factor < value:
        is_prime = (value % trial_factor != 0)
        trial_factor += 1
    if is_prime:
        k += 1
        primorial *= value
        print(primorial + 1, end=" ")
        if k >= n:
            break
    value += 1
