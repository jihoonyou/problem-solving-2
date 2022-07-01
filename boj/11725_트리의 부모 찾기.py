from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
adj_list = [[] for _ in range(n+1)]
p = [0]*(n+1)
for _ in range(n-1):
    v,u = map(int,input().split())
    adj_list[v].append(u)
    adj_list[u].append(v)

def dfs_recursion(cur):
    for nxt in adj_list[cur]:
        if p[cur] == nxt:
            continue
        p[nxt] = cur
        dfs(nxt)

def dfs(node):
    stack = [node]
    while stack:
        cur_node = stack.pop()
        for next_node in adj_list[cur_node]:
            if p[cur_node] == next_node:
                continue
            stack.append(next_node)
            p[next_node] = cur_node

def bfs(node):
    q = deque([node])
    while q:
        cur_node = q.popleft() 
        for next_node in adj_list[cur_node]:
            if p[cur_node] == next_node: # 부모노드인지 확인
                continue
            q.append(next_node)
            p[next_node] = cur_node
dfs_recursion(1)
# dfs(1)
# bfs(1)
for i in range(2,n+1):
    print(p[i])
