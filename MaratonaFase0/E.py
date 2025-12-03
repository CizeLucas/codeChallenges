from math import gcd

y, k = map(int, input().split(' '))

p = [1,y]
while k > 0:
    p[0] += gcd(p[0], p[1])
    k -= 1

print(p[0])