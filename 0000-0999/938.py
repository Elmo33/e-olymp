x1, y1, x2, y2, a = map(float,input().split())

x = (x1 + x2 * a) / (a + 1)

y = (y1 + y2 * a) / (a + 1)

print("%.2f %.2f" %(x,y))
