from math import sqrt

a, b, c = map(int, input().split())

p = (a + b + c) / 2.0
S = sqrt(p * (p - a) * (p - b) * (p - c))
heights = [2 * S / a, 2 * S / b, 2 * S / c]
print(" ".join([str(format(i, '.2f')) for i in heights]))
