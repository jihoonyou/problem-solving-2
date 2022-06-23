from collections import deque
import sys
input = sys.stdin.readline
dr = [(0,1),(0,-1),(1,0),(-1,0)]
t = int(input())

def print2(a):
    for b in a:
        print(b)

for _ in range(t):
    w,h = map(int,input().split())
    arr = []
    for _ in range(h):
        row = input().rstrip()
        arr.append(row)
    dist1 = [[-1 for _ in range(w)] for _ in range(h)]
    dist2 = [[-1 for _ in range(w)] for _ in range(h)]
    fire_q = deque()
    sg_q = deque()
    for y in range(h):
        for x in range(w):
            if arr[y][x] == '*':
                dist1[y][x] = 0
                fire_q.append((y,x))
            if arr[y][x] == '@':
                dist2[y][x] = 0
                sg_q.append((y,x))
    
    while fire_q:
        cur_y, cur_x = fire_q.popleft()
        for dy,dx in dr:
            ny = cur_y + dy
            nx = cur_x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if arr[ny][nx] == '#':
                    continue
                if dist1[ny][nx] >= 0:
                    continue
                fire_q.append((ny,nx))
                dist1[ny][nx] = dist1[cur_y][cur_x] + 1

    isPossible = False
    ans = 0
    while sg_q:
        cur_y, cur_x = sg_q.popleft()
        for dy,dx in dr:
            ny = cur_y + dy
            nx = cur_x + dx
            if ny < 0 or nx < 0 or ny >= h or nx >= w:
                isPossible = True
                ans = dist2[cur_y][cur_x] + 1
                break
            if dist2[ny][nx] >= 0:
                continue
            if arr[ny][nx] == '#':
                continue
            if dist1[ny][nx] != -1 and dist1[ny][nx] <= dist2[cur_y][cur_x] + 1:
                continue
            dist2[ny][nx] = dist2[cur_y][cur_x] + 1
            sg_q.append((ny,nx))
        else:
            continue
        break
    if isPossible:
        print(ans)
    else:
        print("IMPOSSIBLE")