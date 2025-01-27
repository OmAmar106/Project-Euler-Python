import sys,math,cmath,random
from heapq import heappush,heappop
from bisect import bisect_right,bisect_left
from collections import Counter,deque,defaultdict
from itertools import permutations

# functions #
# MOD = 998244353
MOD = 10**9 + 7
RANDOM = random.randrange(2**62)
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return a//gcd(a,b)*b
def w(x):
    return x ^ RANDOM
##

#String hashing : sh/shclass, fenwick sortedlist : fsortl, Number : numtheory, SparseTable : SparseTable
#bucket sorted list : bsortl, segment tree(lazy propogation) : SegmentTree,Other, bootstrap : bootstrap
#binary indexed tree : BIT, segment tree(point updates) : SegmentPoint, Convex Hull : hull, Trie/Treap : Tries
#Combinatorics : pnc, Diophantine Equations : dpheq, Graphs : graphs, DSU : DSU, Geometry: Geometry, FFT: fft
#Template : https://github.com/OmAmar106/Template-for-Competetive-Programming
# input_file = open(r'input.txt', 'r');sys.stdin = input_file

def solve():
    n = int(sys.stdin.readline().strip())
    dp = [1]
    dp.append(1)
    ans = 0
    for i in range(1,n+1):
        dp.append(dp[-1]+dp[-2])
        if dp[-1]>=n:
            break
        if dp[-1]%2==0:
            ans += dp[-1]
    print(ans)
    #L1 = list(map(int, sys.stdin.readline().split()))
    #st = sys.stdin.readline().strip()
solve()