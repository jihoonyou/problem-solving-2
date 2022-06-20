from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = input().rstrip()
    left_stack = []
    right_queue = deque()

    for cmd in l:
        if cmd == '<':
            if left_stack:
                right_queue.appendleft(left_stack.pop())
        elif cmd == '>':
            if right_queue:
                left_stack.append(right_queue.popleft())
        elif cmd == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(cmd)
    print(''.join(left_stack + list(right_queue)))
