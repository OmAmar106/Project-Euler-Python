
arr = [i+1 for i in range(20)]

def gcd(x,y):
    if x%y==0:
        return y
    return gcd(y,x%y)

def lcm(x,y):
    return x*y//gcd(x,y)

lcm1 = 1

for i in arr:
    lcm1 = lcm(lcm1,i)

print(lcm1)