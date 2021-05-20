from math import sqrt
r, x0, y0, x1, y1, x2, y2 = map(int, input().split())
h = abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1)) / sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
line = format(round(2 * (sqrt(r ** 2 - h ** 2)), 5), '.6f')
print(line)
