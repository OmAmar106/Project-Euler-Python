
file = open("0022_names.txt","r")

L = file.readlines()[0].split(',')

L.sort()

ans = 0


def func(st):
    st = list(st)
    st.pop()
    st.pop(0)
    return sum(list(map(lambda x:ord(x.lower())-ord('a')+1,(st))))

for i in range(len(L)):
    ans += (i+1)*func(L[i])

print(ans)