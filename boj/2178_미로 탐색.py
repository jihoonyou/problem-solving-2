'''
https://boj.kr/2178
'''
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
maze = []
dr = [(0,-1), (0,1), (-1,0), (1,0)]

for _ in range(n):
    row = list(map(int,list(input().rstrip())))
    maze.append(row)

dist = [[-1 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque([(0,0)])
    dist[0][0] = 1
    while q:
        cur_y,cur_x = q.popleft()
        for dy,dx in dr:
            ny = cur_y + dy
            nx = cur_x + dx
            if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] == 1 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[cur_y][cur_x] + 1
                q.append((ny,nx))
    return dist[n-1][m-1]
print(bfs())
'''
N,M = map(int,sys.stdin.readline().split())
maze = []
dr = [(0,-1), (0,1), (-1,0), (1,0)]

def bfs():
    deq = deque([(0,0)])
    maze[0][0] = 0
    step = 1
    destination = False
    while deq:
        length = len(deq)
        for _ in range(length):
            y, x = deq.popleft()
            for dy, dx in dr:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] == 1:
                    maze[ny][nx] = 0
                    deq.append((ny,nx))
                    if ny == N -1 and nx == M - 1:
                        destination = True
                        break
            if destination:
                break
        step += 1
        if destination:
            return step



for _ in range(N):
    maze.append(list(map(int,list(sys.stdin.readline().strip()))))

print(bfs())
'''

'''
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
maze = []
dr = [(0,-1), (0,1), (-1,0), (1,0)]

for _ in range(N):
    maze.append(list(map(int,list(input().strip()))))

def maze_solve(maze):
    deq = deque([(0,0)])

    while deq:
        length = len(deq)
        for _ in range(length):
            y,x = deq.popleft()
            for dy,dx in dr:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 1:
                    maze[ny][nx] = maze[y][x] + 1
                    deq.append((ny,nx))
    return maze[N-1][M-1]

print(maze_solve(maze))
'''