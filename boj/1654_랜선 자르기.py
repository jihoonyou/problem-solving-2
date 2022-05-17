'''
https://boj.kr/1654
https://yongmemo.tistory.com/21
'''
import sys
input = sys.stdin.readline

K,N = map(int, input().split())
lines = []

for _ in range(K):
    lines.append(int(input()))

left = 0
right = max(lines)
ans = 1

while left <= right:
    mid = (left + right) // 2
    count = 0
    for line in lines:
        count += line // mid
    
    if count >= N:
        left = mid + 1
        ans = max(ans,mid)
    else:
        right = mid - 1
print(ans)