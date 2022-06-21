from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
positions = list(map(int,input().split()))
dq = deque([i for i in range(1,n+1)])
count = 0

for pos in positions:
    while True:
        if dq[0] == pos:
            dq.popleft()
            break
        if dq.index(pos) <= len(dq) // 2:
            while dq[0] != pos:
                dq.append(dq.popleft())
                count += 1
        else:
            while dq[0] != pos:
                dq.appendleft(dq.pop())
                count += 1
print(count)