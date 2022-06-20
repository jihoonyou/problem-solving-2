from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque(range(1,n+1))

while len(queue) > 1:
    queue.popleft()
    queue.rotate(-1)

print(queue[0])