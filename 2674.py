a, b = map(int, input().split())


def nsd(x, y):
    if y == 0:
        return x
    else:
        return nsd(y, x % y)


c = nsd(abs(a), b)
print(int(a / c), int(b / c))
