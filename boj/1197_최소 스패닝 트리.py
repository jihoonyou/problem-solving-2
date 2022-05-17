'''
https://boj.kr/1197
'''
import sys
import heapq

V,E = map(int,sys.stdin.readline().split())
heap = []
for _ in range(E):
    A,B,C = map(int,sys.stdin.readline().split())
    heapq.heappush(heap, (C,A,B))


parents = [i for i in range(V+1)]

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

result = 0
while heap:
    c,a,b = heapq.heappop(heap)
    if find(a) != find(b):
        union(a,b)
        result += c
print(result)