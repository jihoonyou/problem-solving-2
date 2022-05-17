'''
https://boj.kr/1260
'''
import sys
from collections import deque
input = sys.stdin.readline

N,M,V = map(int,input().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    v1,v2 = map(int,input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

for i in range(N+1):
    adj_list[i].sort()

def DFS(node, step_trace):
    step_trace.append(node)
    for connected_node in adj_list[node]:
        if connected_node not in step_trace:
            DFS(connected_node, step_trace)
    return step_trace

def BFS(node):
    step_trace = []
    step_trace.append(node)
    visited = [0]*(N+1)
    deq = deque([node])
    visited[node] = 1
    while deq:
        current_node = deq.popleft()
        for connected_node in adj_list[current_node]:
            if not visited[connected_node]:
                step_trace.append(connected_node)
                visited[connected_node] = 1
                deq.append(connected_node)
    return step_trace

print(*DFS(V,[]))
print(*BFS(V))