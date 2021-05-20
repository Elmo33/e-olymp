import calendar

k = int(input())
result = 0

def find_day(date):
    day, month, year = (int(i) for i in date.split(' '))
    day_number = calendar.weekday(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    return days[day_number]

def find_13(y1, y2):
    for year in range(int(y1),int(y2)+1):
        for month in range(1,13):
            day = find_day(f"13 {month} {year}")
            if day == "Friday":
                global result
                result+=1


for j in range(0, k):
    year1, year2 = input().split()
    find_13(year1, year2)

print(result)
