'''
https://boj.kr/1992
'''
import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().rstrip())))

def dnc(y,x,n):
    check = graph[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if graph[i][j] != check:
                check = -1
                break
    
    if check == -1:
        print("(", end='')
        n = n // 2
        dnc(y, x, n)
        dnc(y, x + n, n) 
        dnc(y + n, x, n) 
        dnc(y + n, x + n, n)  
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


dnc(0,0,N)