def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


test = input()

A = list(map(int, input().split()))
res = A[0]
for c in A[1::]:
    res = gcd(res, c)
print(res)
