'''
https://boj.kr/10815
'''
import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int,input().split())))
M = int(input())
nums = list(map(int,input().split()))
ans = [0]*len(nums)

for i in range(len(nums)):
    left = 0
    right = len(cards) - 1
    val = nums[i]
    while  left <= right:
        mid = (left+right) // 2
        
        if val > cards[mid]:
            left = mid + 1
        elif val < cards[mid]:
            right = mid - 1
        else:
            ans[i] = 1 
            break

print(*ans)
