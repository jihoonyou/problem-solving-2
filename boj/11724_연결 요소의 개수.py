'''
https://boj.kr/11724
'''
import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

adj_list = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    v1,v2 = map(int,sys.stdin.readline().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

cc = 0
for node in range(1,N+1):
    if not visited[node]:
        deq = deque([node])
        visited[node] = True
        cc += 1      
        while deq:
            current_node = deq.popleft()
            for connected_node in adj_list[current_node]:
                if not visited[connected_node]:
                    deq = deque([connected_node])
                    visited[connected_node] = True
print(cc)

'''
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int,input().split())
adj_list = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    v1,v2 = map(int,input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

def dfs(v):
    visited[v] = 1
    for node in adj_list[v]:
        if not visited[node]:
            dfs(node)

cc = 0
for node in range(1,N+1):
    if not visited[node]:
        cc += 1
        dfs(node)

print(cc)
'''