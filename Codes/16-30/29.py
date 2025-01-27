
ans = 0

s = set()

for i in range(2,101):
    power = [False]*101
    power[0] = True
    power[1] = True
    k = i
    count = 1
    while k*i<101:
        k *= i
        count += 1
        for j in range(2*count,101,count):
            power[j] = True
    # if i==4:
    #     print(power)
    #     print(s,64 in s)
    #     break
    for j in range(len(power)):
        if power[j]:
            continue
        s.add(i**j)

print(len(s))