'''
https://boj.kr/7576
'''
import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int, input().split())

dr = [(-1,0), (1,0), (0,-1), (0,1)]
tomato_box = []
ripe_tomatoes = deque()
count_zero = 0
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(len(row)):
        if row[x] == 1:
            ripe_tomatoes.append((y,x))
        if row[x] == 0:
            count_zero += 1
    tomato_box.append(row)

def bfs(count_zero):
    days = -1
    while ripe_tomatoes:
        length = len(ripe_tomatoes)
        for _ in range(length):
            tomato = ripe_tomatoes.popleft()
            for dy,dx in dr:
                ny = tomato[0] + dy
                nx = tomato[1] + dx
                if 0 <= ny < N and 0 <= nx < M:
                    if tomato_box[ny][nx] == 0:
                        tomato_box[ny][nx] = 1
                        count_zero -= 1
                        ripe_tomatoes.append((ny,nx))
        days += 1
    
    if count_zero:
        return -1
    return days

print(bfs(count_zero))