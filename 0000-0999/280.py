n, m = map(int, input().split())
def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

if n==1 or m==1:
    print(1)
else:
    print(gcd(n,m))
