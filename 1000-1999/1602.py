def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


A = list(map(int, input().split()))

lcm = 1
for i in A:
    lcm = lcm * i // gcd(lcm, i)
print(lcm)
