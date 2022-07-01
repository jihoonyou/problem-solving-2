import heapq
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input())
adj_list = [[] for _ in range(v+1)]
d = [sys.maxsize]*(v+1)
for _ in range(e):
    u,v,w = map(int,input().split())
    adj_list[u].append((w,v))


def dijkstra(start):
    d[start] = 0
    pq = []
    heapq.heappush(pq,(0,start))
    while pq:
        curr_weight,curr_node = heapq.heappop(pq)
        if d[curr_node] != curr_weight:
            continue
        for w,nxt_node in adj_list[curr_node]:
            nxt_weight = w + d[curr_node]
            if d[nxt_node] <= nxt_weight:
                continue
            d[nxt_node] = nxt_weight
            heapq.heappush(pq,(nxt_weight,nxt_node))

dijkstra(k)
for i in range(1,len(d)):
    if d[i] == sys.maxsize:
        print('INF')
    else:
        print(d[i])