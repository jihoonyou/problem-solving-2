'''
https://boj.kr/15650
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [0]*m
isUsed = [False]*(n+1) # 사전에 중복방지

def func(k):
    if k == m:
        print(*arr)
        return

    start_index = 1
    if k != 0:
        start_index = arr[k-1] + 1 # arr에 들어갈 다음 값이 최소 들어간 값보다 크도록
    for i in range(start_index,n+1):
        if not isUsed[i]:
            arr[k] = i
            isUsed[i] = True
            func(k+1)
            isUsed[i] = False

func(0)