'''
https://boj.kr/10866
'''
import sys
from collections import deque
input = sys.stdin.readline

commands = int(input())

deq = deque([])

for _ in range(commands):
    cmd = input()
    if cmd[3] == 'h':
        if cmd[5] == 'f':
            deq.appendleft(int(cmd[11:]))
        else:
            deq.append(int(cmd[10:]))
    elif cmd[3] == '_':
        if cmd[4] == 'f':
            if len(deq):
                print(deq.popleft())
            else:
                print(-1)
        else:
            if len(deq):
                print(deq.pop())
            else:
                print(-1)
    elif cmd[3] == 'e':
        print(len(deq))
    elif cmd[3] == 't':
        if len(deq):
            print(0)
        else:
            print(1)
    elif cmd[3] == 'n':
        if len(deq):
            print(deq[0])
        else:
            print(-1)
    else:
        if len(deq):
            print(deq[-1])
        else:
            print(-1)