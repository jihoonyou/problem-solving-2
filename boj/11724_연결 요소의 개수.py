'''
https://boj.kr/11724
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# ------------ dfs stack (same order with recursion) ------------
n,m = map(int,input().split())

adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

cc = 0
visited = [0]*(n+1)
for node in range(1,n+1):
    stack = []
    if not visited[node]:
        cc += 1
        stack.append(node)

    while stack:
        current_node = stack.pop()
        if visited[current_node]: # 이게 순서맞추는 포인트 그리고 stack에 중복으로 넣고 pop할 때 visit 체크
            continue
        visited[current_node] = 1

        for connected_node in adj_list[current_node]:
            if not visited[connected_node]:
                stack.append(connected_node) # 중복으로 들어감
print(cc)

# ------------ dfs recursion ------------
# n,m = map(int,input().split())

# adj_list = [[] for _ in range(n+1)]
# for _ in range(m):
#     u,v = map(int,input().split())
#     adj_list[u].append(v)
#     adj_list[v].append(u)

# def dfs(node):
#     visited[node] = 1
#     for connected_node in adj_list[node]:
#         if not visited[connected_node]:
#             dfs(connected_node)

# cc = 0
# visited = [0]*(n+1)
# for node in range(1,n+1):
#     if not visited[node]:
#         cc+= 1
#         dfs(node)
# print(cc)

# ------------ dfs stack ------------
# n,m = map(int,input().split())

# adj_list = [[] for _ in range(n+1)]
# for _ in range(m):
#     u,v = map(int,input().split())
#     adj_list[u].append(v)
#     adj_list[v].append(u)

# cc = 0
# visited = [0]*(n+1)
# for node in range(1,n+1):
#     stack = []
#     if not visited[node]:
#         cc += 1
#         stack.append(node)
#         visited[node] = 1
#     while stack:
#         current_node = stack.pop()
#         for connected_node in adj_list[current_node]:
#             if visited[connected_node]:
#                 continue
#             stack.append(connected_node)
#             visited[connected_node] = 1
# print(cc)

# ------------ bfs ------------
# n,m = map(int,input().split())

# adj_list = [[] for _ in range(n+1)]
# for _ in range(m):
#     u,v = map(int,input().split())
#     adj_list[u].append(v)
#     adj_list[v].append(u)

# cc = 0
# visited = [0]*(n+1)
# for node in range(1,n+1):
#     q = deque()
#     if not visited[node]:
#         cc += 1
#         q.append(node)
#         visited[node] = 1
#     while q:
#         current_node = q.popleft()
#         for connected_node in adj_list[current_node]:
#             if visited[connected_node]:
#                 continue
#             q.append(connected_node)
#             visited[connected_node] = 1

# print(cc)
