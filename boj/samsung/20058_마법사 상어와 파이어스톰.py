'''
https://boj.kr/20058
'''
import sys
from collections import deque
input = sys.stdin.readline


dr = [(0,-1),(0,1),(-1,0),(1,0)]
N,Q = map(int,input().split())
grid = []

for _ in range(2**N):
    row = list(map(int,input().split()))
    grid.append(row)


def bfs(y,x):
    q = deque()
    res = 1
    q.append((y,x))
    grid[y][x] = 0

    while q:
        cur_y,cur_x = q.popleft()
        for dy,dx in dr:
            ny = cur_y + dy
            nx = cur_x + dx
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[ny][nx]:
                q.append((ny,nx))
                res += 1
                grid[ny][nx] = 0

    return res

for L in list(map(int,input().split())):
    l_size = 2**L

    for row in range(0,2**N,l_size):
        for col in range(0,2**N,l_size):
            tmp = [grid[i][col:col+l_size] for i in range(row,row+l_size)]
            for r in range(l_size):
                for c in range(l_size):
                        grid[row+c][col+(l_size-1)-r]= tmp[r][c]
    
    # for row in range(0,2**N,l_size):
    #     for col in range(0,2**N,l_size):
    #         tmp = [grid[i][col:col+l_size] for i in range(row,row+l_size)]
    #         tmp = list(zip(*tmp[::-1]))
    #         for r in range(l_size):
    #             for c in range(l_size):
    #                     grid[row+r][col+c]= tmp[r][c]

    # new_board = [[0] * len_board for _ in range(len_board)] # 회전한 Board 저장 용
    # # rotate
    # r_size = 2 ** L # 격자 사이즈
    # for y in range(0, len_board, r_size): # 격자 시작 좌표 y축
    #     for x in range(0, len_board, r_size): # 격자 시작 좌표 x축
    #         for i in range(r_size): # 열 인덱스
    #             for j in range(r_size): # 행 인덱스
    #                 new_board[y + j][x + r_size - i - 1] = board[y + i][x + j] 
    melt = []
    for y in range(len(grid)):
        for x in range(len(grid)):
            cnt = 0
            for dy,dx in dr:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < len(grid) and 0 <= nx < len(grid):
                    if grid[ny][nx] >= 1:
                        cnt += 1
            if cnt < 3 and grid[y][x] != 0:
                melt.append((y,x))
    
    for y,x in melt:
        grid[y][x] -= 1

print(sum( sum(ice_list) for ice_list in grid ))

res = 0
for y in range(len(grid)):
    for x in range(len(grid)):
        if grid[y][x]:
            res = max(res,bfs(y,x))
print(res)