'''
https://boj.kr/11650
'''
import sys
input = sys.stdin.readline

N = int(input())

coordinates = []

for _ in range(N):
    coord = list(map(int,input().split()))
    coordinates.append(coord)

coordinates.sort(key = lambda x : (x[0], x[1]))

for x,y in coordinates:
    print(x,y)