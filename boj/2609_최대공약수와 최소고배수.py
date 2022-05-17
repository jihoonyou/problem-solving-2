'''
https://boj.kr/2609
'''
import sys

X, Y = map(int,sys.stdin.readline().split())

def GCD(x,y):
    while y:
        x,y = y, x%y
    return x

def LCM(x,y, GCD):
    return x*y//GCD

gcd = GCD(X,Y)
print(gcd)
print(LCM(X,Y,gcd))