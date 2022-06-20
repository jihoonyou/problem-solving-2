from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    cmd = input()
    if cmd[1] == 'u': # push
        _,num = cmd.rstrip().split()
        queue.append(num)
    elif cmd[1] == 'r': # front
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[1] == 'i': # size
        print(len(queue))
    elif cmd[1] == 'm': #empty
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[1] == 'a': # back
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif cmd[1] == 'o': # pop
        if queue:
            print(queue.popleft())
        else:
            print(-1)