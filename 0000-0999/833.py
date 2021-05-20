x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
xO, yO = map(int, input().split())

a = (x1 - xO) * (y2 - y1) - (x2 - x1) * (y1 - yO)
b = (x2 - xO) * (y3 - y2) - (x3 - x2) * (y2 - yO)
c = (x3 - xO) * (y1 - y3) - (x1 - x3) * (y3 - yO)


if ((a >= 0) and (b >= 0) and (c >= 0)) or ((a <= 0) and (b <= 0) and (c <= 0)):
    print("In")
else:
    print("Out")
