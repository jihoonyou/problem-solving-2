import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = set(input().split())

cur_min = abs(100-n)

for i in range(0,1000001):
    isComplete = True
    for c in str(i):
        if c in broken:
            isComplete = False
            break
    if isComplete:
        cur_min = min(cur_min, abs(n - i) + len(str(i)))

print(cur_min)
