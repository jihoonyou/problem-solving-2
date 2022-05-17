'''
https://boj.kr/10799
'''
import sys

rods = sys.stdin.readline().strip()
stack = []
count = 0


for idx, parenthesis in enumerate(rods):
    if parenthesis == '(':
        stack.append(parenthesis)
    else:
        if rods[idx-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)

