
n = 1001

mat = [[0]*n for i in range(n)]

val = 1
start = [n//2,n//2]

dirs = ((0,1),(1,0),(0,-1),(-1,0))

i = 0
dir1 = 1

ans = 0

while True:
    try:
        for k in range(2):
            for j in range(dir1):
                mat[start[0]][start[1]] = val
                if start[0]==start[1] or sum(start)+1==n:
                    ans += val
                start[0] += dirs[i][0]
                start[1] += dirs[i][1]
                val += 1
            i += 1
            i %= 4
        dir1 += 1
    except:
        break

# print(mat)
print(ans)