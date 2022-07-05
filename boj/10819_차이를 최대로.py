from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
ans = 0
for per in list(permutations(arr,n)):
    cur = 0
    for i in range(n-1):
        cur += abs(per[i] - per[i+1])
    ans = max(ans,cur)
print(ans)