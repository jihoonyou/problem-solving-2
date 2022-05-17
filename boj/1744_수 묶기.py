'''
https://boj.kr/1744
'''
import sys
input = sys.stdin.readline

N = int(input())

positive = []
negative = []
res = 0

for _ in range(N):
    n = int(input())
    if n > 1:
        positive.append(n)
    elif n == 1:
        res += 1
    else:
        negative.append(n)

positive.sort(reverse= True)
negative.sort()

if len(positive) % 2 == 0:
    for i in range(0,len(positive),2):
        res += positive[i] * positive[i+1]
else:
    for i in range(0,len(positive) - 1, 2):
        res += positive[i] * positive[i+1]
    res += positive[-1]

if len(negative) % 2 == 0:
    for i in range(0,len(negative),2):
        res += negative[i] * negative[i+1]
else:
    for i in range(0,len(negative) - 1,2):
        res += negative[i] * negative[i+1]
    res += negative[-1]

print(res)