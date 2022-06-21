import sys
input = sys.stdin.readline

n = int(input())
count = 0
for _ in range(n):
    words = input().rstrip()
    stack = []
    for c in words:
        if not stack:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
    if not stack:
        count += 1
print(count)
