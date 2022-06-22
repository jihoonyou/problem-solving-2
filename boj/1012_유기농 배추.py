from collections import deque
import sys
input = sys.stdin.readline
dr = [(0,1),(0,-1),(1,0),(-1,0)]
t = int(input())

def bfs(y,x):
    q = deque([(y,x)])
    arr[y][x] = 0
    while q:
        cur_y,cur_x = q.popleft()
        for dy,dx in dr:
            ny = cur_y + dy
            nx = cur_x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if arr[ny][nx] == 0:
                continue
            q.append((ny,nx))
            arr[ny][nx] = 0

for _ in range(t):
    m,n,k = map(int,input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x,y = map(int,input().split())
        arr[y][x] = 1
    count = 0
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1:
                count += 1
                bfs(r,c)
    print(count)