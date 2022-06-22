from collections import deque
import sys
input = sys.stdin.readline
dr = [(-1,0),(1,0),(0,1),(0,-1)]
r,c = map(int,input().split())

q1 = deque()
q2 = deque()
dist1 = [[-1 for _ in range(c)] for _ in range(r)]
dist2 = [[-1 for _ in range(c)] for _ in range(r)]

maze = []
for _ in range(r):
    row = list(list(input().rstrip()))
    maze.append(row)

for y in range(r):
    for x in range(c):
        if maze[y][x] == 'F':
            q1.append((y,x))
            dist1[y][x] = 0
        if maze[y][x] == 'J':
            q2.append((y,x))
            dist2[y][x] = 0
while q1:
    y,x = q1.popleft()
    for dy,dx in dr:
        ny = dy + y
        nx = dx + x
        if ny < 0 or nx < 0 or nx >= c or ny >= r:
            continue
        if maze[ny][nx] == '#' or dist1[ny][nx] >= 0:
            continue
        dist1[ny][nx] = dist1[y][x] + 1
        q1.append((ny,nx))

isPossible = False
ans = 0
while q2:
    y,x = q2.popleft()
    for dy,dx in dr:
        ny = dy + y
        nx = dx + x
        if ny < 0 or nx < 0 or nx >= c or ny >= r:
            ans = dist2[y][x] + 1
            break
        if maze[ny][nx] == '#' or dist2[ny][nx] >= 0:
            continue
        if dist1[ny][nx] != -1 and dist1[ny][nx] <= dist2[y][x] + 1:
            continue
        dist2[ny][nx] = dist2[y][x] + 1
        q2.append((ny,nx))
    else:
        continue
    isPossible = True
    break
if isPossible:
    print(ans)
else:
    print('IMPOSSIBLE')
