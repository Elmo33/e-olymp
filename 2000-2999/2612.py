temp = 0
need = 1
a, b = map(int, input().split())
while need:
    if a >= b:
        temp = temp + a // b
        a = a % b
    else:
        temp = temp + b // a
        b = b % a
    if a == 0 or b == 0:
        need = 0

print(temp)
