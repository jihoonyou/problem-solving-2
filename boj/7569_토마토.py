from collections import deque
import sys
input = sys.stdin.readline
dr = [(0,0,1),(0,0,-1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]

m,n,h = map(int,input().split())
tomatoes = []
dist = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

for _ in range(h): # z
    tomato_x_y = []
    for _ in range(n): # y
        row = list(map(int,input().split()))
        tomato_x_y.append(row)
    tomatoes.append(tomato_x_y)

q = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomatoes[z][y][x] == 0:
                dist[z][y][x] = -1
            if tomatoes[z][y][x] == 1:
                q.append((z,y,x))
                dist[z][y][x] = 0

while q:
    z,y,x = q.popleft()
    for dz,dy,dx in dr:
        nz = z + dz
        ny = y + dy
        nx = x + dx
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if dist[nz][ny][nx] >= 0:
                continue
            q.append((nz,ny,nx))
            dist[nz][ny][nx] = dist[z][y][x] + 1

isComplete = True
cur_max = -1
for z in range(h):
    for y in range(n):
        for x in range(m):
            if dist[z][y][x] == -1:
                isComplete = False
                cur_max = -1
                break
            cur_max = max(cur_max,dist[z][y][x])
        else:
            continue
        break
    else:
        continue
    break
print(cur_max)
