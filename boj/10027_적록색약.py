from collections import deque
import sys
input = sys.stdin.readline
dr = [(0,1),(0,-1),(1,0),(-1,0)]

n = int(input())
vis1 = [[0 for _ in range(n)] for _ in range(n)]
vis2 = [[0 for _ in range(n)] for _ in range(n)]

def bfs(y,x,vis,color,flag = False):
    q = deque([(y,x)])
    vis[y][x] = 1
    color_pool = []
    if flag:
        if color == 'R' or color == 'G':
            color_pool = ['R','G']
        else:
            color_pool = ['B']
    else:
        color_pool = [color]
    while q:
        curr_y,curr_x = q.popleft()
        for dy,dx in dr:
            ny = dy + curr_y
            nx = dx + curr_x
            if (0 <= ny < n and 0 <= nx < n) and not vis[ny][nx] and arr[ny][nx] in color_pool:
                q.append((ny,nx))
                vis[ny][nx] = 1
arr = []
for _ in range(n):
    row = list(input().strip())
    arr.append(row)

count1 = 0
for r in range(n):
    for c in range(n):
        if not vis1[r][c]:
            color = arr[r][c]
            count1 += 1
            bfs(r,c,vis1,color)

count2 = 0
for r in range(n):
    for c in range(n):
        if not vis2[r][c]:
            color = arr[r][c]
            count2 += 1
            bfs(r,c,vis2,color,True)

print(count1,count2)
