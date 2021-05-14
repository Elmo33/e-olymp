x1, y1, z1, x2, y2, z2, x3, y3, z3 = map(int, input().split())


def length(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


def solve(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    a = length(x1, y1, z1, x2, y2, z2)
    b = length(x2, y2, z2, x3, y3, z3)
    c = length(x3, y3, z3, x1, y1, z1)
    p = (a + b + c) / 2
    r = ((p - a) * (p - b) * (p - c) / p) ** 0.5
    R = a * b * c / (4 * (p * (p - a) * (p - b) * (p - c)) ** 0.5)
    if r == 0:
        print(0)
    return round(r ** 2 / R ** 2, 3)


res = solve(x1, y1, z1, x2, y2, z2, x3, y3, z3)
print(res if res != 0 else "Zero!")
