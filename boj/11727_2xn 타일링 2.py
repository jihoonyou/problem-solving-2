import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(1001)

# 테이블 정의
# dp[i] = 2 * i 타일을 채우는 방법의 수

# 초기값
dp[1] = 1
dp[2] = 3

for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 10007

print(dp[n])