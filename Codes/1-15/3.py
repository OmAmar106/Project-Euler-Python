n = int(input())

start = 2

ans = 1
n1 = n
while start*start<=n and n1!=1:
    while n1%start==0:
        n1 //= start
        ans = max(ans,start)
    start += 1
ans = max(ans,n1)

print(ans)