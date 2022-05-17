'''
https://boj.kr/2667
'''
import sys

N = int(sys.stdin.readline())
apartments = []
apartments_info = []

for _ in range(N):
    apartments.append(list(map(int,list(sys.stdin.readline().rstrip()))))

def dfs(y,x):
    apartments[y][x] = 0
    apartments_info[-1] += 1

    if y > 0 and apartments[y - 1][x] == 1:
        dfs(y-1,x)
    if y + 1 < len(apartments) and apartments[y+1][x] == 1:
        dfs(y+1,x)
    if x > 0 and apartments[y][x - 1] == 1:
        dfs(y, x-1)
    if x + 1 < len(apartments[0]) and apartments[y][x+1] == 1:
        dfs(y,x+1)
    

for i in range(N):
    for j in range(len(apartments[i])):
        if apartments[i][j] == 1:
            apartments_info.append(0)
            dfs(i,j)
apartments_info.sort()
print(len(apartments_info))
for info in apartments_info:
    print(info)


'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dr = [(-1,0), (1,0), (0,-1), (0,1)]
apartments = []
apartment_info = []

for _ in range(N):
    apartments.append(list(map(int,list(input().rstrip()))))


def dfs(y,x):
    apartment_info[-1] += 1
    apartments[y][x] = 0

    for dy,dx in dr:
        ny = y + dy
        nx = x + dx
        if nx >= 0 and ny >= 0 and nx < N and ny < N and apartments[ny][nx] == 1:
            dfs(ny,nx)

for y in range(N):
    for x in range(N):
        if apartments[y][x] == 1:
            apartment_info.append(0)
            dfs(y,x)
apartment_info.sort()

print(len(apartment_info))
for info in apartment_info:
    print(info)
'''