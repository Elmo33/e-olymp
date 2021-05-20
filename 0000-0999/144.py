x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())


def check(a1, b1, a2, b2, a3, b3):
    return True if (a1 - a2) * (a3 - a2) + (b1 - b2) * (b3 - b2) == 0 else False


k = 0
k += 1 if check(x1, y1, x2, y2, x3, y3) else 0
k += 1 if check(x2, y2, x3, y3, x4, y4) else 0
k += 1 if check(x3, y3, x4, y4, x1, y1) else 0
k += 1 if check(x4, y4, x1, y1, x2, y2) else 0

print(k)
