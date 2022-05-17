import sys
input = sys.stdin.readline

N,M = map(int,input().split())
univ = [0] + list(input().split())
dating = []
edges = []
parents = list(range(N+1))

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(M):
    u,v,d = map(int,input().split())
    edges.append((d,u,v))

edges.sort()

for d,u,v in edges:
    if find(u) != find(v) and univ[u] != univ[v]:
        union(u,v)
        dating.append(d)
if len(dating) == N-1:
    print(sum(dating))
else:
    print(-1)