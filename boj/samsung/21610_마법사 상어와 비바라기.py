'''
https://boj.kr/21610
'''
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dr = [(0,0), (0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)] # 8방향, 0은 dummy
clouds = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)] # 구름 생기는 곳
d_dr = [(-1,-1),(-1,1),(1,1),(1,-1)] # diagnal dir

grid = []
for _ in range(N):
    row = list(map(int,input().split()))
    grid.append(row)


for _ in range(M):
    move = list(map(int,input().split()))
    
    next_clouds = []
    visited = set()
    for y,x in clouds: # step1
        dy,dx = dr[move[0]]
        s = move[1]
        ny = (y + dy*s) % N
        nx = (x + dx*s) % N
        next_clouds.append((ny,nx))
        visited.add((ny,nx))
    
    for y,x in next_clouds: # step2
        grid[y][x] += 1
    
    clouds = [] # step3


    for y,x in next_clouds: # step4
        for dy,dx in d_dr:
            ny = y + dy
            nx = x + dx
            if 0 <= nx < N and 0 <= ny < N:
                if grid[ny][nx] > 0:
                    grid[y][x] += 1

    for y in range(N): # step5
        for x in range(N):
            if grid[y][x] >= 2 and (y,x) not in visited:
                grid[y][x] -= 2
                clouds.append((y,x))

res = 0
for row in grid:
    res += sum(row)

print(res)
