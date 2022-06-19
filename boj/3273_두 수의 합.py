import sys
input = sys.stdin.readline

n = int(input())
ns = sorted(map(int,input().split()))
x = int(input())
count = 0
l = 0 
r = len(ns)- 1
while l < r:
    total = ns[l] + ns[r]
    if total == x:
        count += 1
        l += 1
    elif total < x:
        l += 1
    else:
        r -= 1
print(count)