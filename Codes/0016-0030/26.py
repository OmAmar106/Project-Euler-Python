d = {}
fans = 0
for i in range(1,1001):
    currem = 1
    ans = []
    dp = {}
    count = 0
    while currem and currem not in dp:
        dp[currem] = count
        currem *= 10
        currem %= i
        count += 1
    if currem:
        fans = max(fans,count-dp[currem])

print(fans)