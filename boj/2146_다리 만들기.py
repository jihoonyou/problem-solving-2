from collections import deque
import sys
input = sys.stdin.readline
dr = [(0,1),(0,-1),(1,0),(-1,0)]

n = int(input())
if n == 1:
    print(0)
    exit()

country_map =[]

for _ in range(n):
    row = list(map(int,input().split()))
    country_map.append(row)

def grouping_island(y,x,group):
    q = deque([(y,x)])
    country_map[y][x] = group
    while q:
        cur_y, cur_x = q.popleft()
        for dy,dx in dr:
            ny = dy + cur_y
            nx = dx + cur_x
            if 0 <= ny < n and 0 <= nx < n:
                if country_map[ny][nx] == 1:
                    country_map[ny][nx] = group
                    q.append((ny,nx))

def make_bridge(group):
    global ans

    q = deque()
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if country_map[y][x] == group:
                q.append((y,x))
                dist[y][x] = 0
    while q:
        cur_y, cur_x = q.popleft()
        for dy,dx in dr:
            ny = dy + cur_y
            nx = dx + cur_x
            if 0 <= ny < n and 0 <= nx < n:
                if dist[ny][nx] >= 0:
                    continue
                if country_map[ny][nx] == 0:
                    dist[ny][nx] = dist[cur_y][cur_x] + 1
                    q.append((ny,nx))                    
                if country_map[ny][nx] and country_map[ny][nx] != group:
                    ans = min(ans, dist[cur_y][cur_x])
                    return


group = 2
for y in range(n):
    for x in range(n):
        if country_map[y][x] == 1:
            grouping_island(y,x,group)
            group += 1
ans = float('inf')
for g in range(2,group):
    make_bridge(g)

print(ans)