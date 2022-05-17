'''
https://boj.kr/2751
'''
import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

for n in sorted(nums):
    print(n)
