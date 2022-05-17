'''
https://boj.kr/1707
'''
import sys
from collections import deque

K = int(sys.stdin.readline())


def bfs(V):
    visited[V] = 1
    deq = deque([V])
    while deq:
        current_node = deq.popleft()
        prev_color = visited[current_node]
        for connected_node in adj_list[current_node]:
            if not visited[connected_node]:
                visited[connected_node] = 3 - prev_color
                deq.append(connected_node)
            elif visited[connected_node] == prev_color:
                return False
    return True


for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    adj_list = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        X, Y = map(int, sys.stdin.readline().split())
        adj_list[X].append(Y)
        adj_list[Y].append(X)
    is_bipartite_graph = True
    for i in range(1, V+1):
        if not visited[i]:
            is_bipartite_graph = bfs(i)
            if not is_bipartite_graph:
                break
    if is_bipartite_graph:
        print('YES')
    else:
        print('NO')