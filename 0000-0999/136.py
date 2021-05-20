def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


x1, y1, x2, y2 = map(int, input().split())
X = abs(x1 - x2)
Y = abs(y1 - y2)

print(gcd(X, Y) + 1)
