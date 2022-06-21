from collections import deque
from heapq import heappush
import sys
input = sys.stdin.readline
IDX,VAL = 0,1
n,l = map(int,input().split())

a = [0] + list(map(int,input().split()))
ans = []
dq = deque()

for i in range(1,len(a)):
    while dq and dq[-1][VAL] >= a[i]:
        dq.pop()
    dq.append((i,a[i]))
    while dq and i - dq[0][IDX] >= l:
        dq.popleft()
    ans.append(dq[0][VAL])
print(*ans)