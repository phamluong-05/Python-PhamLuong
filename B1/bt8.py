from math import factorial
n = int(input('n ='))
for i in range(n):
    for j in range(n-i):
        print(end=" ")
    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()