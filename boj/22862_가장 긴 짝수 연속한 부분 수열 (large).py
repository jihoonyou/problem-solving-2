import sys
input = sys.stdin.readline

s,k= map(int,input().split())
nums = list(map(int,input().split()))

k_used_count = 0
en = 0
if nums[en] % 2 != 0:
    k_used_count += 1
ans = 0
for st in range(s):
    while en < s - 1 and (nums[en+1] % 2 + k_used_count) <= k:
        en += 1
        k_used_count += (nums[en] % 2)
    ans = max(ans, en - st + 1 - k_used_count)
    k_used_count -= (nums[st] % 2)
print(ans)
