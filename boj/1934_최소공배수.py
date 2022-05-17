'''
https://boj.kr/1934
'''
import sys

def GCD(x,y):
    while y:
        x,y = y, x%y
    return x

def LCM(x,y,gcd):
    return x*y//gcd

T = int(sys.stdin.readline())

for _ in range(T):
    X,Y = map(int,sys.stdin.readline().split())
    print(LCM(X,Y,GCD(X,Y)))
