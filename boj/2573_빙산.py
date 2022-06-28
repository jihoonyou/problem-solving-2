from collections import deque
import sys
input = sys.stdin.readline
dr = [(0,1),(0,-1),(1,0),(-1,0)]

n,m = map(int,input().split())
iceberg = []
for _ in range(n):
    row = list(map(int,input().split()))
    iceberg.append(row)

def count_pieces(y,x,visited):
    q = deque([(y,x)])
    visited[y][x] = 1
    while q:
        cur_y, cur_x = q.popleft()
        for dy,dx in dr:
            ny = dy + cur_y
            nx = dx + cur_x
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and iceberg[ny][nx]:
                q.append((ny,nx))
                visited[ny][nx] = 1

def iceberg_melt(y,x,visited,iceberg):
    visited[y][x] = 1
    water_count = 0 
    for dy,dx in dr:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < n and 0 <= nx < m:
            if visited[ny][nx]:
                continue
            if iceberg[ny][nx]== 0:
                water_count += 1

    iceberg[y][x] -= water_count
    if iceberg[y][x] < 0:
        iceberg[y][x] = 0


ans = 0
year = 0
while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for y in range(n):
        for x in range(m):
            if not visited[y][x] and iceberg[y][x] > 0:
                count += 1
                count_pieces(y,x,visited)
    
    if count >= 2:
        ans = year
        break
    if count == 0:
        break

    visited = [[0 for _ in range(m)] for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if iceberg[y][x] > 0:    
                iceberg_melt(y,x,visited,iceberg)
    year += 1

print(ans)

# from collections import deque
# import sys
# input = sys.stdin.readline
# dr = [(0,1),(0,-1),(1,0),(-1,0)]

# n,m = map(int,input().split())
# iceberg = []
# for _ in range(n):
#     row = list(map(int,input().split()))
#     iceberg.append(row)

# def count_pieces(y,x,visited):
#     q = deque([(y,x)])
#     visited[y][x] = 1
#     while q:
#         cur_y, cur_x = q.popleft()
#         for dy,dx in dr:
#             ny = dy + cur_y
#             nx = dx + cur_x
#             if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and iceberg[ny][nx]:
#                 q.append((ny,nx))
#                 visited[ny][nx] = 1

# def iceberg_melt(iceberg):
#     zeros = [[0 for _ in range(m)] for _ in range(n)]
#     for y in range(n):
#         for x in range(m):
#             if iceberg[y][x] == 0: continue
#             for dy,dx in dr:
#                 ny = dy + y
#                 nx = dx + x            
#                 if 0 <= ny < n and 0 <= nx < m:
#                     if iceberg[ny][nx] == 0:
#                         zeros[y][x] += 1
#     for i in range(n):
#         for j in range(m):
#             if iceberg[i][j] > 0:
#                 iceberg[i][j] = max(0, iceberg[i][j]- zeros[i][j])

# ans = 0
# year = 0
# while True:
#     visited = [[0 for _ in range(m)] for _ in range(n)]
#     count = 0
#     for y in range(n):
#         for x in range(m):
#             if not visited[y][x] and iceberg[y][x] > 0:
#                 count += 1
#                 count_pieces(y,x,visited)
    
#     if count >= 2:
#         ans = year
#         break
#     if count == 0:
#         break

#     # visited = [[0 for _ in range(m)] for _ in range(n)]

#     iceberg_melt(iceberg)
#     year += 1

# print(ans)