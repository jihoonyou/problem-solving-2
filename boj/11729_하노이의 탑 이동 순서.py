'''
https://boj.kr/11729
'''
import sys
input = sys.stdin.readline

n = int(input())
def hanoi(n, fro, to, inter):
    if n == 1:
        print(fro, to)
    else:
        hanoi(n - 1, fro, inter, to)
        print(fro, to)
        hanoi(n - 1, inter, to, fro)
print(2**n-1)
hanoi(n,1,3,2)