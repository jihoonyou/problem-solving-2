from collections import deque
import sys
input = sys.stdin.readline
dr = [(0,0,1),(0,0,-1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]

while True:
    l,r,c = map(int,input().split())
    if l==0 and r==0 and c==0:
        break 
    dist = [[[-1 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    building = []
    for _ in range(l):
        temp = []
        for _ in range(r):
            row = list(input().rstrip())
            temp.append(row)
        input() # 공백 제거
        building.append(temp)
    q = deque()
    for z in range(l):
        for y in range(r):
            for x in range(c):
                if building[z][y][x] == 'S':
                    dist[z][y][x] = 0
                    q.append((z,y,x))
    ans = -1
    while q:
        z,y,x = q.popleft()
        for dz,dy,dx in dr:
            nz = z + dz
            ny = y + dy
            nx = x + dx
            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c:
                if building[nz][ny][nx] == '#':
                    continue
                if dist[nz][ny][nx] >= 0:
                    continue
                if building[nz][ny][nx] == 'E':
                    ans = dist[z][y][x] + 1
                    break
                q.append((nz,ny,nx))
                dist[nz][ny][nx] = dist[z][y][x] + 1
        else:
            continue
        break
    
    if ans != -1:
        print(f'Escaped in {ans} minute(s).')
    else:
        print('Trapped!')
