'''
https://boj.kr/1647
'''
import sys

N,M = map(int,sys.stdin.readline().split())

edges = []
for _ in range(M):
    a,b,w = map(int,sys.stdin.readline().split())
    edges.append((w,a,b))

edges.sort()
parents = [i for i in range(N+1)]

def find(a):
    if parents[a] == a:
        return parents[a]
    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


cost = []
for w, a, b in edges:
    if find(a) != find(b):
        union(a,b)
        cost.append(w)
print(sum(cost[:-1]))
