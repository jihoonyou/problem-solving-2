'''
https://boj.kr/9466
https://suri78.tistory.com/128
'''
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    choice = [0] + list(map(int,sys.stdin.readline().split()))
    visited = [0]*(n+1)

    group = 1
    for i in range(1,n+1):
        while visited[i] == 0:
            visited[i] = group
            i = choice[i]
        while visited[i] == group:
            visited[i] = -1
            i = choice[i]
        group += 1
    print(n - visited.count(-1))
