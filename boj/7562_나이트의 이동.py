from collections import deque
import sys
input = sys.stdin.readline
dr = [(-1,-2),(-2,-1),(1,-2),(2,-1),(-2,1),(-1,2),(1,2),(2,1)]

t = int(input())
for _ in range(t):
    l = int(input())
    dist = [[-1 for _ in range(l)] for _ in range(l)]
    knight = list(map(int,input().split()))
    destination = list(map(int,input().split()))

    q = deque([(knight[0],knight[1])])
    dist[knight[0]][knight[1]] = 0
    while q:
        y,x = q.popleft()
        for dy,dx in dr:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or nx >= l or ny >= l:
                continue
            if dist[ny][nx] >= 0:
                continue
            q.append((ny,nx))
            dist[ny][nx] = dist[y][x] + 1
        else:
            continue
        break
    print(dist[destination[0]][destination[1]])