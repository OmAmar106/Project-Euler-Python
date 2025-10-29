
d = {
    0:31,
    1:28,
    2:31,
    3:30,
    4:31,
    5:30,
    6:31,
    7:31,
    8:30,
    9:31,
    10:30,
    11:31
}

def leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)

ans = 0
cur = 1

for i in range(1900,2001):
    for j in range(12):
        if cur==0 and i!=1900:
            ans += 1
        days = d[j]
        if j==1 and leap(i):
            days += 1
        cur += days
        cur %= 7

print(ans)