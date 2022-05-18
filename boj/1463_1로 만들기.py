from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1) # i를 1로 만들기 위해 필요한 연산 사용 횟수의 최소값 <- 테이블 정의
# dp[1] = 0 초기값 

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1 # 1로 더하기
    if i % 2 == 0: # 2로 나누어질 경우
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0: # 3으로 나누어질 경우
        dp[i] = min(dp[i], dp[i//3]+1)
    
print(dp[n])
# BFS solution
# ans = 0
# N = int(input())
# dr = [1,2,3]
# cnts = [0]*(N+1)

# q = deque()
# q.append(1)

# while q:
#     cur = q.popleft()

#     if cur == N:
#         ans = cnts[cur]
#         break
    
#     for i in range(len(dr)):
#         nx = 0
#         if i == 0:
#             nx = cur + dr[i]
#         else:
#             nx = cur * dr[i]
    
#         if nx > N:
#             continue

#         if cnts[nx] == 0:
#             cnts[nx] = cnts[cur] + 1

#         q.append(nx)

# print(ans)