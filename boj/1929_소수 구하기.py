'''
https://boj.kr/1929
'''
import sys
input = sys.stdin.readline

M,N = map(int,input().split())

sieve = [False,False] + [True]*(N-1)

for i in range(2,N+1):
    if sieve[i]:
        for j in range(i*2,N+1,i):
            sieve[j] = False

for num in range(M,N+1):
    if sieve[num]:
        print(num)