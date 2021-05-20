from math import acos, sqrt, pi

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
c = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)

alpha = acos((b * b + c * c - a * a) / (2 * b * c))
betta = acos((a * a + c * c - b * b) / (2 * a * c))
gamma = acos((a * a + b * b - c * c) / (2 * a * b))

alpha = alpha * 180 / pi
betta = betta * 180 / pi
gamma = gamma * 180 / pi

print(format(round(alpha if alpha > betta else betta if betta > gamma else gamma, 6), '.6f'))
