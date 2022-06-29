import sys
input = sys.stdin.readline

n= int(input())
prime = []
sieve = [False,False] + [True]*(n-1)

def getPrimes(n):
    for i in range(2,n+1):
        if sieve[i]:
            for j in range(i*2,n+1,i):
                sieve[j] = False

    for num in range(n+1):
        if sieve[num]:
            prime.append(num)

getPrimes(n)
window_start, window_sum = 0,0
ans = 0
for window_end in range(len(prime)):
    window_sum += prime[window_end]
    if window_sum == n:
        ans += 1
    while window_sum >= n:
        window_sum -= prime[window_start]
        window_start += 1
        if window_sum == n:
            ans += 1

print(ans)