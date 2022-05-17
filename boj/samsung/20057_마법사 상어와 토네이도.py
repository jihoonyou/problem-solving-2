'''
https://boj.kr/20057
'''
import sys
input = sys.stdin.readline

N = int(input())
left = [(-1,-1,0.1),(1,-1,0.1),(-1,0,0.07),(1,0,0.07),(-1,1,0.01),(1,1,0.01),(0,-2,0.05),(-2,0,0.02),(2,0,0.02),(0,-1,0)]
right = [(y,-x,z) for y,x,z in left]
down = [(-x,y,z) for y,x,z in left]
up = [(x,y,z) for y,x,z in left]

grid = []
for _ in range(N):
    row = list(map(int,input().split()))
    grid.append(row)

def solve(cnt,dy,dx,tornado_dr):
    global res, curr_y, curr_x

    for _ in range(cnt):
        curr_y += dy
        curr_x += dx
        total = 0
        for _dy,_dx,ratio in tornado_dr:
            ny = curr_y + _dy
            nx = curr_x + _dx
            if ratio == 0:
                new_sand = grid[curr_y][curr_x] - total
            else:
                new_sand = int(grid[curr_y][curr_x] * ratio)
                total += new_sand
            if 0 <= ny < N and 0 <= nx < N:
                grid[ny][nx] += new_sand
            else:
                res += new_sand

curr_y,curr_x = N//2,N//2
res = 0
for i in range(1,N+1):
    if i == N:
        solve(i-1,0,-1,left)
        break
    if i % 2 != 0:
        solve(i,0,-1,left)
        solve(i,1,0,down)
    else:
        solve(i,0,1,right)
        solve(i,-1,0,up)

print(res)