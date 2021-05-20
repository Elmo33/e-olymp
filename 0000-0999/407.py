def solve(cases):
    for i in range(cases):
        flowers = ["G", "C", "V"]
        days = int(input())
        for k in range(days):
            flowers.append(flowers.pop(1))
            flowers.insert(0, flowers.pop(1))
        print("".join(flowers))
solve(int(input()))
