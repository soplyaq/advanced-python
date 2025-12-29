def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A = int(input())
B = int(input())
C = int(input())
D = int(input())

num = A*D - B*C
den = B*D

g = gcd(abs(num), den)

print(num//g, "/", den//g)
