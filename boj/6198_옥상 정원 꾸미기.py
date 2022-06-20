# monotone stack
import sys
input = sys.stdin.readline

n = int(input())
buildings = []

for _ in range(n):
    buildings.append(int(input()))

stack = []
count = 0
for height in buildings:
    while stack and stack[-1] <= height:
        stack.pop()

    count += len(stack)
    stack.append(height)

print(count)
