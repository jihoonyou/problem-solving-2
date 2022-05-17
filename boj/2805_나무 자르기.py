'''
https://boj.kr/2805
'''
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
trees = list(map(int,input().split()))
left = 0
right = max(trees)
res = 0

while left <= right:
    mid = (left+right) // 2
    total_length = 0
    for tree in trees:
        if tree > mid:
            total_length += (tree - mid)
    
    if total_length >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)