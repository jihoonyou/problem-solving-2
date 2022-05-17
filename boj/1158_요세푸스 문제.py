'''
https://boj.kr/1158
'''
import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(range(1, N+1))
josephus_permutation = []
step = 0

while nums:
    step = (step + (K-1)) % len(nums)
    josephus_permutation.append(nums.pop(step))

print('<' + ', '.join(str(x) for x in josephus_permutation) + '>')