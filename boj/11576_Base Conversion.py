'''
https://boj.kr/11576
'''
import sys

A, B = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())
A_num = list(map(int,sys.stdin.readline().split()))
base10 = 0
count = 0
B_num = []

for idx in range(N-1, -1, -1):
    base10 += A_num[idx]*(A**count)
    count += 1

while base10:
    B_num.append(str(base10%B))
    base10 = base10 // B

print(' '.join(B_num[::-1]))