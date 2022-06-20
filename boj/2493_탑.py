import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int,input().split()))
stack = []
res = []
for i in range(1,n+1):
    height = towers[i-1]
    while stack:
        if stack[-1][0] <= height:
            stack.pop()
        else:
            break
    if stack:
        res.append(stack[-1][1])
    else:
        res.append(0)
    stack.append((height,i))

print(' '.join(map(str,res)))