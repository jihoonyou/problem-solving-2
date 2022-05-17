'''
https://boj.kr/2110
'''
import sys
input = sys.stdin.readline

N,C = map(int,input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()

start = 1
end = houses[-1] - houses[0]
ans = 0

while start <= end:
    mid = (end+start) // 2

    prev = houses[0]
    count = 1
    for i in range(1,len(houses)):
        if houses[i] - prev >= mid:
            count += 1
            prev = houses[i]
    
    if count >= C:
        ans = max(ans,mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)