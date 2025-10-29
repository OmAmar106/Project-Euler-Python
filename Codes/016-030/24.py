
from itertools import permutations

L = [0,1,2,3,4,5,6,7,8,9]

count = 0

for row in permutations(L):
    count += 1
    if count==1000000:
        print(row)
        exit()