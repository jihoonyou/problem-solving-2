from collections import deque
import sys
input = sys.stdin.readline

dr = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

N,M,K = map(int,input().split())

position = deque()
grid = [[deque() for _ in range(N)] for _ in range(N)]


def move():
    num_of_fireballs = len(position)
    next_grid = []
    for _ in range(num_of_fireballs):
        y,x = position.popleft()
        grid_length = len(grid[y][x])
        for _ in range(grid_length): # step 1
            _m, _s, _d = grid[y][x].popleft()
            dy,dx = dr[_d]
            ny = (y + dy*_s) % N
            nx = (x + dx*_s) % N
            position.append((ny,nx))
            next_grid.append([ny,nx,_m,_s,_d])


    for _r, _c, _m, _s, _d in next_grid:
        grid[_r][_c].append([_m,_s,_d])

    for y in range(N):
        for x in range(N):
            if len(grid[y][x]) >= 2:
                total_mass, total_speed = 0,0
                odd = False
                even = False
                new_dr = None
                for _m,_s,_d in grid[y][x]:
                    total_mass += _m
                    total_speed += _s
                    if _d % 2 == 0:
                        even = True
                    else:
                        odd = True
                new_mass = total_mass // 5
                new_speed = total_speed // len(grid[y][x])
                grid[y][x] = deque()
                if new_mass > 0:
                    if (not even and odd) or (not odd and even):
                        new_dr = [0,2,4,6]
                    else:
                        new_dr = [1,3,5,7]
                    
                    for _dr in new_dr:
                        grid[y][x].append([new_mass,new_speed,_dr])

for _ in range(M):
    r, c, m, s, d = map(int,input().split())
    position.append((r-1,c-1))
    grid[r-1][c-1].append([m,s,d])

for _ in range(K):
    move()

res = 0
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            for _m, _s, _d in grid[i][j]:
                res += _m

print(res)