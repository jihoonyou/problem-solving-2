import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = sorted(map(int,input().split()))
arr = [0]*m

def func(k):
    if k == m:
        print(*arr)
        return
    for i in range(len(nums)):
        if k != 0 and arr[k-1] > nums[i]:
            continue
        arr[k] = nums[i]
        func(k+1)
func(0)