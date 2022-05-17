'''
https://boj.kr/10610
'''
import sys
input = sys.stdin.readline
N = input().rstrip()
N = sorted(list(N), reverse=True)

if '0' not in N:
    print(-1)
else:
    sum = 0
    for n in N:
        sum += int(n)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(N))
