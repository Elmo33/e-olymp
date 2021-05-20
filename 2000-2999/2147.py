vertices = int(input())
total = 0

x, y = map(int, input().split())
x1 = x
y1 = y

for i in range(vertices - 1):
    x2, y2 = map(int, input().split())
    total = total + (x1 + x2) * (y2 - y1)
    x1 = x2
    y1 = y2
total = total + (x + x2) * (y - y2)
print('{:.1f}'.format(abs(total)/2))
