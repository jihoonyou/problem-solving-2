import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == '.':
        break
    stack = []
    for c in sentence:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                print('no')
                break
            else:
                stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                print('no')
                break
            else:
                stack.pop()
    else:
        if stack:
            print('no')
        else:
            print('yes')
