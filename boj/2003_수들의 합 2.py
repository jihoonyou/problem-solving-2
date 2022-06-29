import sys
input = sys.stdin.readline

n,m= map(int,input().split())
nums = list(map(int,input().split()))
window_start,total = 0,0
ans = 0
for window_end in range(len(nums)):
    total += nums[window_end]
    if total == m:
        ans += 1
    while total >= m:
        total -= nums[window_start]
        window_start += 1
        if total == m:
            ans += 1
print(ans)