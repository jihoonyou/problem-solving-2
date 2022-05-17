'''
https://boj.kr/4963
'''
import sys

sys.setrecursionlimit(10000)
def dfs(y, x):
    islands[y][x] = 0

    if y > 0 and islands[y-1][x] == 1:
        dfs(y-1, x)
    if y+1 < len(islands) and islands[y+1][x] == 1:
        dfs(y+1, x)
    if x > 0 and islands[y][x-1] == 1:
        dfs(y, x-1)
    if x+1 < len(islands[0]) and islands[y][x+1] == 1:
        dfs(y, x+1)
    if y > 0 and x > 0 and islands[y-1][x-1] == 1:
        dfs(y-1, x-1)
    if y+1 < len(islands) and x+1 < len(islands[0]) and islands[y+1][x+1] == 1:
        dfs(y+1,x+1)
    if y+1 < len(islands) and x > 0 and islands[y+1][x-1] == 1:
        dfs(y+1, x-1)
    if x+1 < len(islands[0]) and y > 0 and islands[y-1][x+1] == 1:
        dfs(y-1,x+1)

while True:
    number_of_islands = 0
    W, H = map(int, sys.stdin.readline().split())
    if W+H == 0:
        break
    islands = []
    for _ in range(H):
        islands.append(list(map(int, sys.stdin.readline().split())))
    for y in range(H):
        for x in range(W):
            if islands[y][x] == 1:
                number_of_islands += 1
                dfs(y, x)
    print(number_of_islands)