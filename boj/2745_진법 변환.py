'''
https://boj.kr/2745
'''
import sys

base_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, base = sys.stdin.readline().split()
base = int(base)
result = 0
count = 0

for idx in range(len(N)-1,-1,-1):
    result += base_map.index(N[idx])*(base**count)
    count += 1

print(result)
