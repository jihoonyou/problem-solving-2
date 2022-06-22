from collections import deque
import sys

input = sys.stdin.readline
dist = [-1]*100001

n,k = map(int,input().split())

dist[n] = 0
q = deque([n])

while dist[k] == -1:
    cur = q.popleft()
    for next in [cur-1,cur+1,cur*2]:
        if next < 0 or next > 100000:
            continue
        if dist[next] != -1:
            continue
        dist[next] = dist[cur] + 1
        q.append(next)

print(dist[k])