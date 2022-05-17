'''
https://boj.kr/1978
'''
import sys
input = sys.stdin.readline

MAX_N = 1000
sieve = [False,False] + [True]*(MAX_N - 1)

for i in range(2,MAX_N+1):
    if sieve[i]:
        for j in range(i*2,MAX_N+1,i):
            sieve[j] = False

N = int(input())
prime_nums = list(map(int,input().split()))
count = 0
for num in prime_nums:
    if sieve[num]:
        count += 1
print(count)