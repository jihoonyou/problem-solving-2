'''
https://boj.kr/2089
'''
import sys

N = int(sys.stdin.readline())

if not N:
    print('0')
    exit()

res=''
while N:
    if N % -2 == 0:
        res = '0' + res 
        N = N//-2
    else:
        res = '1'+ res
        N = N//-2 + 1
print(res)