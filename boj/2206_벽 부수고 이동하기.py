# https://kscodebase.tistory.com/66
from collections import deque
import sys
input = sys.stdin.readline
dr = [(0,1),(0,-1),(1,0),(-1,0)]

n,m = map(int,input().split())
arr = []
for _ in range(n):
    row = list(map(int,list(input().rstrip())))
    arr.append(row)

dist = [[[-1]*2 for _ in range(m)] for _ in range(n)]

def bfs(y,x):
    q = deque()
    q.append((y,x,0))
    dist[0][0][0] = 1
    dist[0][0][1] = 1

    while q:
        y,x,broken = q.popleft()
        if y == n - 1 and x == m - 1:
            return dist[y][x][broken]
        for dy,dx in dr:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < n and 0 <= nx < m:
                # destination

                if dist[ny][nx][broken] >= 0:
                    continue
                if arr[ny][nx] == 0:
                    q.append((ny,nx,broken))
                    dist[ny][nx][broken] = dist[y][x][broken] + 1
                else:
                    if broken == 1:
                        continue
                    dist[ny][nx][1] = dist[y][x][broken] + 1
                    q.append((ny,nx,1))
    return -1
print(bfs(0,0))