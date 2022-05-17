'''
https://boj.kr/10451
'''
import sys

T = int(sys.stdin.readline())

def dfs(V):
    visited[V] = True
    connected_node = adj_list[V]
    if not visited[connected_node]:
        dfs(connected_node)

for _ in range(T):
    N = int(sys.stdin.readline())
    adj_list = [0]+ list(map(int,sys.stdin.readline().split()))
    visited = [False]*(N+1)
    count = 0
    for node in range(1,N+1):
        if not visited[node]:
            count += 1
            dfs(node)
    print(count)
    