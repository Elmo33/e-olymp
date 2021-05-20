m = input()
k = input().split()
for i in range(int(m)-1):
    k.append(k.pop(0))
print(" ".join(k))
