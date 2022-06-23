from collections import deque
import sys
input = sys.stdin.readline
dr = [(0,1),(0,-1),(1,0),(-1,0)]

m,n,k = map(int,input().split())
arr = [[0 for _ in range(n)] for _ in range(m)]

def bfs(y,x):
    q = deque([(y,x)])
    arr[y][x] = 1
    cnt = 0
    while q:
        cur_y,cur_x = q.popleft()
        cnt += 1
        for dy,dx in dr:
            ny = dy + cur_y
            nx = dx + cur_x
            if 0 <= ny < m and 0 <= nx < n:
                if arr[ny][nx] == 1:
                    continue
                q.append((ny,nx))
                arr[ny][nx] = 1
    return cnt

count = 0
areas = []
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())

    for y in range(y1,y2):
        for x in range(x1,x2):
            calc_y = len(arr)- 1 - y
            arr[calc_y][x] = 1

for y in range(m):
    for x in range(n):
        if arr[y][x] == 0:
            count += 1
            areas.append(bfs(y,x))
print(count)
print(*sorted(areas))