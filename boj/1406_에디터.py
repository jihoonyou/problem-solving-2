'''
https://boj.kr/1406
'''
import sys
from collections import deque

left_stack = list(sys.stdin.readline().rstrip())
right_queue = deque()
M = int(sys.stdin.readline())

for _ in range(M):
    cmd = sys.stdin.readline()
    if cmd[0] == 'L':
        if len(left_stack):
            right_queue.appendleft(left_stack.pop())
    elif cmd[0] == 'D':
        if len(right_queue):
            left_stack.append(right_queue.popleft())
    elif cmd[0] == 'B':
        if len(left_stack):
            left_stack.pop()
    else:
        left_stack.append(cmd[2])

print(''.join(left_stack + list(right_queue)))