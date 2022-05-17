'''
https://boj.kr/1850
'''
import sys

A,B = map(int,sys.stdin.readline().split())

while B:
    A,B = B,A%B
print('1'*A)