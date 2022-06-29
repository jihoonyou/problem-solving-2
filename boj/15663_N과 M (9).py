from operator import isub
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = sorted(map(int,input().split()))
isUsed = [0]*m
arr = [0]*m

def func(k):
    if k == m:
        print(*arr)
        return
    tmp = 0
    for i in range(n):
        if not isUsed[i] and tmp != nums[i]:
            isUsed[i] = 1
            arr[k] = nums[i]
            tmp = nums[i]
            func(k+1)
            isUsed[i] = 0
func(0)