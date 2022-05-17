'''
https://boj.kr/10816
'''
import sys
input = sys.stdin.readline

M = int(input())
dic = {}

cards = list(map(int,input().split()))
for card in cards:
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

N = int(input())
nums = list(map(int,input().split()))

for num in nums:
    if num in dic:
        print(dic[num], end=' ')
    else:
        print(0, end=' ')
