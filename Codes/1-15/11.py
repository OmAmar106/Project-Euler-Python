
L = []

for i in range(20):
    L.append(list(map(int,input().split())))

def func(a,b,c,d):
    return a*b*c*d

ans = 0

for i in range(len(L)):
    for j in range(len(L)):
        if i+3<len(L):
            ans = max(ans,func(L[i][j],L[i+1][j],L[i+2][j],L[i+3][j]))
        if j+3<len(L):
            ans = max(ans,func(L[i][j],L[i][j+1],L[i][j+2],L[i][j+3]))
        if i+3<len(L) and j+3<len(L):
            ans = max(ans,func(L[i][j],L[i+1][j+1],L[i+2][j+2],L[i+3][j+3]))
        if i+3<len(L) and j-3>=0:
            ans = max(ans,func(L[i][j],L[i+1][j-1],L[i+2][j-2],L[i+3][j-3]))

print(ans)
