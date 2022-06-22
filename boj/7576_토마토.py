'''
https://boj.kr/7576
'''
from collections import deque
import sys
input = sys.stdin.readline
dr = [(0,1),(0,-1),(1,0),(-1,0)]

m,n = map(int,input().split())
dist = [[0 for _ in range(m)] for _ in range(n)]
tomatoes = []

for _ in range(n):
    row = list(map(int,input().split()))
    tomatoes.append(row)

ripe_tomatoes = deque()
for y in range(n):
    for x in range(m):
        if tomatoes[y][x] == 0:
            dist[y][x] = -1
        if tomatoes[y][x] == 1:
            ripe_tomatoes.append((y,x))

while ripe_tomatoes:
    y,x = ripe_tomatoes.popleft()
    for dy,dx in dr:
        ny = y + dy
        nx = x + dx
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        if dist[ny][nx] >= 0:
            continue
        dist[ny][nx] = dist[y][x] + 1
        ripe_tomatoes.append((ny,nx))
ans = 0
for y in range(n):
    for x in range(m):
        if dist[y][x] == -1:
            ans = dist[y][x]
            break
        else:
            ans = max(ans,dist[y][x])
    else:
        continue
    break
print(ans)
'''
import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int, input().split())

dr = [(-1,0), (1,0), (0,-1), (0,1)]
tomato_box = []
ripe_tomatoes = deque()
count_zero = 0
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(len(row)):
        if row[x] == 1:
            ripe_tomatoes.append((y,x))
        if row[x] == 0:
            count_zero += 1
    tomato_box.append(row)

def bfs(count_zero):
    days = -1
    while ripe_tomatoes:
        length = len(ripe_tomatoes)
        for _ in range(length):
            tomato = ripe_tomatoes.popleft()
            for dy,dx in dr:
                ny = tomato[0] + dy
                nx = tomato[1] + dx
                if 0 <= ny < N and 0 <= nx < M:
                    if tomato_box[ny][nx] == 0:
                        tomato_box[ny][nx] = 1
                        count_zero -= 1
                        ripe_tomatoes.append((ny,nx))
        days += 1
    
    if count_zero:
        return -1
    return days

print(bfs(count_zero))
'''