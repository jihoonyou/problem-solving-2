'''
https://boj.kr/1920
'''
import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(map(int,input().split()))

m = int(input())
m = list(map(int,input().split()))

def binary_search(target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start+end) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return 1
    return 0
        

for target in m:
    print(binary_search(target))
