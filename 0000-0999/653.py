a, b, c = map(float, input().split())

if a+b>c and a+c>b and b+c>a:
    if a*a+b*b>c*c and a*a+c*c>b*b and b*b+c*c>a*a:
        print("ACUTE")
    if a*a+b*b<c*c or a*a+c*c<b*b or b*b+c*c<a*a:
        print("OBTUSE")
    if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("RIGHT")
else:
    print("IMPOSSIBLE")
