'''
https://boj.kr/11728
'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
res = []

a_index, b_index = 0,0

while a_index < len(A) and b_index < len(B):
    if A[a_index] > B[b_index]:
        res.append(B[b_index])
        b_index += 1
    else:
        res.append(A[a_index])
        a_index += 1
    
if a_index == len(A):
    res.extend(B[b_index:])
else:
    res.extend(A[a_index:])

print(*res)