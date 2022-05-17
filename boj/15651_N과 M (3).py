'''
https://boj.kr/15651
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [0]*(m)

def func(k):
    if k == m:
        print(*arr)
        return
    
    for i in range(1,n+1):
        arr[k] = i
        func(k+1)

func(0)