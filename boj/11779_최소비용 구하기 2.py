import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

adj_list = [[] for _ in range(n+1)]
d = [sys.maxsize]*(n+1)
pre = [0]*(n+1)
for _ in range(m):
    v,u,w = map(int,input().split())
    adj_list[v].append((w,u))
st,en = map(int,input().split())

def dijkstra(start):
    hq = []
    d[start] = 0
    heapq.heappush(hq,(0,start))
    while hq:
        curr_weight,cur_node = heapq.heappop(hq)
        if d[cur_node] != curr_weight:
            continue
        for w,nxt_node in adj_list[cur_node]:
            nxt_weight = w + d[cur_node]
            if d[nxt_node] <= nxt_weight:
                continue
            d[nxt_node] = nxt_weight
            heapq.heappush(hq,(nxt_weight,nxt_node))
            pre[nxt_node] = cur_node

dijkstra(st)

path = []
cur = en
while cur != st:
    path.append(cur)
    cur = pre[cur]
path.append(cur)

print(d[en])
print(len(path))
print(*reversed(path))