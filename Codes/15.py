
dp = [[0]*21 for i in range(21)]

dp[-1][-1] = 1

for i in range(20,-1,-1):
    for j in range(20,-1,-1):
        if i+1<21:
            dp[i][j] += dp[i+1][j] 
        if j+1<21:
            dp[i][j] += dp[i][j+1]

print(dp[0][0])