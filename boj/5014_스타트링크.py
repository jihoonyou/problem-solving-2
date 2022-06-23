from collections import deque
import sys
input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())

building = [-1 for _ in range(f+1)]
up_down = [u,-d]
building[s] = 0
q = deque([s])

while building[g] == -1 and q:
    current_floor = q.popleft()
    for move in up_down:
        next_floor = current_floor + move
        if next_floor <= 0 or next_floor > f:
            continue
        if building[next_floor] != -1:
            continue
        building[next_floor] = building[current_floor] + 1
        q.append(next_floor)
if building[g] != -1:
    print(building[g])
else:
    print('use the stairs')