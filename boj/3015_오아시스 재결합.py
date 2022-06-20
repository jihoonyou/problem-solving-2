# 참고 - https://0902.tistory.com/57
import sys
input = sys.stdin.readline
HEIGHT,CNT = 0,1

n = int(input())
stack = []
answer = 0

for _ in range(n):
    height = int(input())
    while stack and stack[-1][HEIGHT] < height:
        answer += stack.pop()[CNT]

    if not stack:
        stack.append((height,1))
        continue

    if stack[-1][HEIGHT] == height:
        cnt = stack.pop()[CNT]
        answer += cnt

        if stack:
            answer += 1

        stack.append((height,cnt+1))
    else:
        stack.append((height,1))
        answer += 1
print(answer)