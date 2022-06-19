import sys
input = sys.stdin.readline

_ = input()
nums = list(map(int,input().split()))
v = int(input())
freq = [0]*201

for n in nums:
    temp = 100 + n
    freq[temp] += 1

print(freq[100+v])