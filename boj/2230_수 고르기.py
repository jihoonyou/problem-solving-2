import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()
ans = float('inf')
en = 0
for st in range(len(nums)):
    while en < n and nums[en] - nums[st] < m:
        en+=1
    if en == n:
        break
    ans = min(ans,nums[en]-nums[st])

print(ans)