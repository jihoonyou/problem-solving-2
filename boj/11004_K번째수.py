'''
https://boj.kr/11004
'''
import sys
input = sys.stdin.readline

N,A = map(int,input().split())

nums = sorted(map(int,input().split()))

print(nums[A-1])
