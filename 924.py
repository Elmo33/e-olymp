from math import pi, sqrt

s, r1 = map(float, input().split())

print(format(round(sqrt(r1 ** 2 - s / pi), 2), '.2f'))
