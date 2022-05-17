'''
https://boj.kr/10989
https://www.acmicpc.net/board/view/26132
'''
import sys
input = sys.stdin.readline
MAX_NUM = 10001

N = int(input())
nums = [0]*MAX_NUM

for _ in range(N):
    nums[int(input())] += 1

for i in range(1,MAX_NUM):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)