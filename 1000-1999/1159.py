days = int(input())
for i in range(1, 32):
    for m in range(1, 13):
        if i * 12 + m * 31 == days:
            date = ""
            if i < 10:
                date += "0"
            date += f"{i}/"
            if m < 10:
                date += "0"
            date += str(m)
            print(date)
