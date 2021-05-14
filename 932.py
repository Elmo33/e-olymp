from math import sqrt

s, a = map(int, input().split())

d = a ** 2 + 8 * s
dk = sqrt(d)
h = (-a + dk) / 2

print(h)
