from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cmds = input().rstrip()
    isReversed = False
    isError = False
    n = int(input())
    raw_arr = input().rstrip()
    dq = deque(map(int,raw_arr[1:len(raw_arr)-1].split(','))) if n > 0 else deque()
    
    for cmd in cmds:
        if cmd == 'R':
            isReversed = not isReversed
        else:
            if dq:
                if isReversed:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                isError = True
                break
    if isError:
        print('error')
    else:

        if isReversed:
            dq.reverse()
            dq = map(str,dq)    
            print('['+','.join(dq)+']')
        else:
            dq = map(str,dq)    
            print('['+','.join(dq)+']')