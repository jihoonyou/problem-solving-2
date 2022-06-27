'''
https://boj.kr/9466
https://suri78.tistory.com/128
'''
from collections import deque
import sys
input = sys.stdin.readline
NOT_VISISITED = 0
CYCLE_IN = -1

def run(index):
    cur = index
    while True:
        state[cur] = index
        cur = team_choice[cur]
        if state[cur] == index:
            while state[cur] != CYCLE_IN:
                state[cur] = CYCLE_IN
                cur = team_choice[cur]
            return
        elif state[cur] != NOT_VISISITED:
            return


t = int(input())
for _ in range(t):
    n = int(input())
    team_choice = [0] + list(map(int,input().split()))
    state = [0] * (n+1)
    for i in range(1,n+1):
        if state[i] == NOT_VISISITED:
            run(i)
    print(n - state.count(CYCLE_IN))

# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):
#     n = int(sys.stdin.readline())
#     choice = [0] + list(map(int,sys.stdin.readline().split()))
#     visited = [0]*(n+1)

#     group = 1
#     for i in range(1,n+1):
#         while visited[i] == 0:
#             visited[i] = group
#             i = choice[i]
#         while visited[i] == group:
#             visited[i] = -1
#             i = choice[i]
#         group += 1
#     print(n - visited.count(-1))
