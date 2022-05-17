'''
https://boj.kr/14499
https://wisdom-990629.tistory.com/entry/C-%EB%B0%B1%EC%A4%80-14499%EB%B2%88-%EC%A3%BC%EC%82%AC%EC%9C%84-%EA%B5%B4%EB%A6%AC%EA%B8%B0
'''
import sys
input = sys.stdin.readline
dr = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
dice = [0 for _ in range(7)]

def dice_move(d):
    if d == 1: # 4,2,1,6,5,3
        dice[1],dice[3],dice[4],dice[6] = dice[4],dice[1],dice[6],dice[3]
    elif d == 2:
        dice[1],dice[3],dice[4],dice[6] = dice[3],dice[6],dice[1],dice[4]
    elif d == 3:
        dice[1],dice[2],dice[5],dice[6] = dice[2],dice[6],dice[1],dice[5]
    elif d == 4:
        dice[1],dice[2],dice[5],dice[6] = dice[5],dice[1],dice[6],dice[2]


n,m,x,y,k = map(int,input().split())
_map = []
for _ in range(n):
    row = list(map(int,input().split()))
    _map.append(row)

cmds = list(map(int,input().split()))

for cmd in cmds:
    dx,dy = dr[cmd]
    nx = x + dx
    ny = y + dy
    if 0 <= nx < n and 0 <= ny < m:
        x = nx
        y = ny
        dice_move(cmd)
        if _map[x][y] != 0:
            dice[6] = _map[x][y]
            _map[x][y] = 0
        else:
            _map[x][y] = dice[6]

        print(dice[1])

