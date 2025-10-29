ans = {}
ans[1] = 1

fans = 1
maxi = 1

for i in range(1,10**6 + 1):
    count = 0
    k = i
    while k not in ans:
        count += 1
        if k%2==0:
            k //= 2
        else:
            k = 3*k+1
    ans[i] = count+ans[k]
    if ans[i]>maxi:
        maxi = ans[i]
        fans = i

print(fans)