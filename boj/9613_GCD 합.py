'''
https://boj.kr/9613
'''
import sys

T = int(sys.stdin.readline())

def GCD(x,y):
    while y:
        x,y = y,x%y
    return x

for _ in range(T):
    nums = list(map(int, sys.stdin.readline().split()))[1:]
    result = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            result += GCD(nums[i], nums[j])
    print(result)
