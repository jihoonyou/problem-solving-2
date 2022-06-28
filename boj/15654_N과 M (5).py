import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = sorted(map(int,input().split()))
arr = [0]*m
isUsed = [0]*n

def func(k):
    if k == m:
        print(*arr)
        return
    for i in range(len(nums)):
        if isUsed[i]:
            continue
        arr[k] = nums[i]
        isUsed[i] = 1
        func(k+1)
        isUsed[i] = 0

func(0)