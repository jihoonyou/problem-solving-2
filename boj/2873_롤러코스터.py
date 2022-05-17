'''
https://boj.kr/2873
'''
import sys
input = sys.stdin.readline

R,C = map(int,input().split())
land = []

for _ in range(R):
    land.append(list(map(int,input().split())))

if R % 2 != 0:
    print(('R'*(C-1) + 'D' + 'L'*(C-1) + 'D') * (R//2) + 'R'*(C-1))
elif C % 2 != 0:
    print(('D'*(R-1) + 'R' + 'U'*(R-1) + 'R') * (C//2) + 'D'*(R-1))
else:
    low = 1000
    position = [-1,-1]
    for i in range(R):
        if i % 2 == 0:
            for j in range(1,C,2):
                if low > land[i][j]:
                    low = land[i][j]
                    position = [i,j]
        else:
            for j in range(0,C,2):
                if low > land[i][j]:
                    low = land[i][j]
                    position = [i,j]
                    
    res = ('D'*(R-1) + 'R' + 'U'*(R-1) + 'R') * (position[1] //2)
    
    x = 2 * (position[1] // 2)
    y = 0
    x_bound = 2 * (position[1] // 2) + 1

    while x != x_bound or y != R - 1:
        if x != x_bound and [y, x_bound] != position:
            x += 1
            res += 'R'
        elif x == x_bound and [y, x_bound - 1] != position:
            x -= 1
            res += 'L'
        if y != R - 1:
            y += 1
            res += 'D'

    res += ('R' + 'U' * (R - 1) + 'R' + 'D' * (R - 1)) * ((C - position[1] - 1) // 2)
    
    print(res)