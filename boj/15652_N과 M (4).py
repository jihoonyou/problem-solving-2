import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [0]*m

def func(k):
    if k == m:
        print(*arr)
        return
    start_index = 1
    if k != 0:
        start_index = arr[k-1]
    for i in range(start_index,n+1):
        arr[k] = i # arr.append
        func(k+1)
        # arr.pop
func(0)