import sys
input = sys.stdin.readline

n,s = map(int,input().split())
nums = list(map(int,input().split()))

window_sum,window_start = 0,0
ans = float('inf')

for window_end in range(len(nums)):
    window_sum += nums[window_end]
    
    while window_sum >= s:
        ans = min(ans, window_end - window_start + 1)
        window_sum -= nums[window_start]
        window_start += 1

if ans == float('inf'):
    ans = 0
print(ans)
    
# en = 0
# partial_sum = nums[en]
# ans = float('inf')
# for st in range(len(nums)):
#     while en < n and partial_sum <s:
#         en += 1
#         if en != n:
#             partial_sum += nums[en]
        
#     if en == n:
#         break
#     ans = min(ans, en-st + 1)

#     partial_sum -= nums[st]
# if ans == float('inf'):
#     ans = 0
# print(ans)