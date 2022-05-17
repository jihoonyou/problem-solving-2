'''
https://boj.kr/21609
'''
import sys
from collections import deque
input = sys.stdin.readline

dr = [(0,-1), (0,1), (-1,0), (1,0)]

def rot_right(board):
    return [list(elem) for elem in list(zip(*board[::-1]))]

def rot_left(board):
    return [list(elem) for elem in list(zip(*board))[::-1]]

def rot_print(board):
    print('----')
    for rr in board:
        print(rr)
    print('----')

def gravity(board):
    for col in range(N):
        for row in range(N-2,-1,-1):
            if board[row][col] != -1:
                r = row
                while True:
                    if 0 <= r+1 < N and board[r+1][col] == -2:
                        board[r+1][col], board[r][col] = board[r][col], board[r+1][col]
                        r += 1
                    else:
                        break
def bfs(y,x):

    q = deque()
    q.append((y,x))
    color = board[y][x]
    blocks = []
    blocks.append((y,x))
    rainbow_blocks = []
    block_count = 1
    rainbow_count = 0

    while q:
        cy,cx = q.popleft()

        for dy,dx in dr:
            ny = cy + dy
            nx = cx + dx
            
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if board[ny][nx] == color:
                    blocks.append((ny,nx))
                    block_count += 1
                    q.append((ny,nx))
                    visited[ny][nx] = True
                elif board[ny][nx] == 0:
                    block_count += 1
                    rainbow_count += 1
                    rainbow_blocks.append((ny,nx))
                    q.append((ny,nx))
                    visited[ny][nx] = True
    
    for ry,rx in rainbow_blocks:
        visited[ry][rx] = False

    return [block_count, rainbow_count, blocks + rainbow_blocks, (y, x)]

N,M = map(int,input().split())
board = []
score = 0

for _ in range(N):
    board.append(list(map(int,input().split())))

while True:

    visited = [[False for _ in range(N)] for _ in range(N)]
    boards = []
    for y in range(N):
        for x in range(N):
            if board[y][x] != -1 and board[y][x] != 0 and board[y][x] != -2 and not visited[y][x]:
                visited[y][x] = True
                board_info = bfs(y,x)
                if board_info[0] >= 2:
                    boards.append(board_info)

    if not boards:
        break

    boards.sort(key = lambda x:(-x[0], -x[1], -x[3][0], -x[3][1]))

    for ry, rx in boards[0][2]:
        board[ry][rx] = -2
    score += boards[0][0]**2
    
    gravity(board)
    board = rot_left(board)
    gravity(board)
print(score)