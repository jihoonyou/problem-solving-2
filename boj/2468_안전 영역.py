from collections import deque
import sys
input = sys.stdin.readline
dr = [(0,1),(0,-1),(1,0),(-1,0)]

n = int(input())

area = []
max_height = 0
for _ in range(n):
    row = list(map(int,input().split()))
    max_height = max(max_height,max(row))
    area.append(row)

def bfs(y,x,limit):
    q = deque([(y,x)])
    visited[y][x] = 1
    while q:
        cur_y,cur_x = q.popleft()
        for dy,dx in dr:
            ny = cur_y + dy
            nx = cur_x + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if area[ny][nx] > limit:
                    visited[ny][nx] = 1
                    q.append((ny,nx))
max_safe_area = 0
for limit in range(0,max_height):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    for y in range(n):
        for x in range(n):
            if area[y][x] > limit and not visited[y][x]:
                bfs(y,x,limit)
                count += 1
    max_safe_area = max(max_safe_area,count)
print(max_safe_area)