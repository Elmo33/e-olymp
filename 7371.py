a, b, c, d = map(int, input().split())


def nsd(x, y):
    if y == 0:
        return x
    else:
        return nsd(y, x % y)


a = b * c + a * d
b = b * d
c = nsd(abs(a), b)
print(int(a / c), int(b / c))
