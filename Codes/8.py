
ans = 0

L = [""]

for i in range(19):
    L[-1] += input()

for i in range(len(L)):
    for j in range(len(L[i])-13):
        k1 = 1
        for k in range(j,j+13):
            k1 *= int(L[i][k])
        ans = max(ans,k1)

print(ans)
