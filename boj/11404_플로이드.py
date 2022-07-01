import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c

for i in range(n):
    graph[i][i] = 0

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

floyd_warshall()

for i in range(n):
    for j in range(n):
        if graph[i][j] == sys.maxsize:
            graph[i][j] = 0

for row in graph:
    print(*row)
