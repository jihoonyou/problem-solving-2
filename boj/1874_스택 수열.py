import sys
input = sys.stdin.readline

n = int(input())
res = []
count = 1
stack = []
isPossible = True

for _ in range(n):
    x = int(input())

    while count <= x:
        stack.append(count)
        res.append('+')
        count += 1
    
    if stack[-1] == x:
        stack.pop()
        res.append('-')
    else:
        isPossible = False
if isPossible:
    for v in res:
        print(v)
else:
    print('NO')