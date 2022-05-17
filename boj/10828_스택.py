'''
https://boj.kr/10828
'''
import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    command = input()
    if command[:2] == 'pu':
        stack.append(int(command[5:]))
    elif command[:2] == 'to':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command[:2] == 'si':
        print(len(stack))
    elif command[:2] == 'em':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack.pop())
        else:
            print(-1)
