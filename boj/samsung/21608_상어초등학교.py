'''
https://boj.kr/21608
'''
import sys
input = sys.stdin.readline

N = int(input())
dr = [(-1,0), (1,0), (0,-1), (0,1)]

classroom = [[0]*N for _ in range(N)]
student_info = {}

for _ in range(N*N):
    info = list(map(int,input().split()))
    student_info[info[0]] = info[1:]
    
    max_y,max_x = 0,0
    max_empty = -1
    max_like = -1
    for i in range(N):
        for j in range(N):
            if classroom[i][j] == 0:
                empty_cnt = 0
                friend_cnt = 0

                for y,x in dr:
                    ny = i + y
                    nx = j + x
                    if 0 <= ny < N and 0 <= nx < N:
                        if classroom[ny][nx] in info:
                            friend_cnt += 1
                        if classroom[ny][nx] == 0:
                            empty_cnt += 1

                if max_like < friend_cnt or (max_like == friend_cnt and max_empty < empty_cnt):
                    max_y = i
                    max_x = j
                    max_like = friend_cnt
                    max_empty = empty_cnt
    
    classroom[max_y][max_x] = info[0]

res = 0
happy = [0,1,10,100,1000]
for y in range(N):
    for x in range(N):
        cnt = 0
        _info = student_info[classroom[y][x]]
        for dy,dx in dr:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if classroom[ny][nx] in _info:
                    cnt +=1
        res += happy[cnt]
        
print(res)
