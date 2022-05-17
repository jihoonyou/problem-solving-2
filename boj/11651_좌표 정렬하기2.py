'''
https://boj.kr/11651
'''
import sys
intput = sys.stdin.readline

N = int(input())

coordinates = []

for _ in range(N):
    coord = list(map(int,input().split()))
    coordinates.append(coord)

for x,y in sorted(coordinates, key = lambda x : (x[1], x[0])):
    print(x,y)