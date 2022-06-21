from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dr = [(0,-1),(0,1),(1,0),(-1,0)]
paper = []
for _ in range(n):
    drawing = list(map(int,input().split()))
    paper.append(drawing)

def bfs(y,x):
    q = deque()
    q.append((y,x))
    paper[y][x] = 0
    cnt = 1
    while q:
        curr_y,curr_x = q.popleft()
        for dy,dx in dr:
            ny = curr_y + dy
            nx = curr_x + dx
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if paper[ny][nx] == 0:
                continue
            q.append((ny,nx))
            paper[ny][nx] = 0
            cnt += 1
    return cnt

count = 0
current_max = 0
for y in range(n):
    for x in range(m):
        if paper[y][x]:
            count += 1
            temp_max = bfs(y,x)
            current_max = max(temp_max,current_max)

print(count)
print(current_max)