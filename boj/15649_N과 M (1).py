import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [0]*m
isUsed = [False]*(n+1) # 편의를 위해 하나 더 추가 했음

def func(k): # k는 arr의 index 그리고 base_case에서 arr에 들어간 갯수
    if k == m: #len(arr) == m
        print(*arr)
        return
    
    for i in range(1,n+1):
        if not isUsed[i]:
            arr[k] = i # arr.append
            isUsed[i] = True
            func(k+1)
            isUsed[i] = False
						# arr.pop
func(0)