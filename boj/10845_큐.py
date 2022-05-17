'''
https://boj.kr/10845
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque([])

for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if command[1] == 'u':
        queue.append(command[5:])
    elif command[1] == 'o':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[1] == 'i':
        print(len(queue))
    elif command[1] == 'm':
        if queue:
            print(0)
        else:
            print(1)
    elif command[1] == 'r':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)
