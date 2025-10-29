ones = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
tens = {10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,
        20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}

ans = 0
for i in range(1,1000):
    n = i
    words = 0
    if n>=100:
        words += ones[n//100] + 7
        if n%100:
            words += 3
        n %= 100
    if n>=20:
        words += tens[(n//10)*10]
        n %= 10
    if 10<=n<20:
        words += tens[n]
        n = 0
    if n:
        words += ones[n]
    ans += words

ans += 11
print(ans)
