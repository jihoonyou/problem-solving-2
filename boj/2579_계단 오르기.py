import sys
input = sys.stdin.readline

dp = [0 for _ in range(301)]
s = [0]
n = int(input())
total = 0
for i in range(n):
    point = int(input())
    s.append(point)
    total += point

if n <= 2:
    print(total)
else:

    dp[1] = s[1]
    dp[2] = s[2]
    dp[3] = s[3]

    for i in range(3,n+1):
        dp[i] = min(dp[i-2],dp[i-3]) + s[i]
    ans = total - min(dp[i-2],dp[i-1])
    print(ans)

# dp = [[0 for _ in range(3)] for _ in range(301)]
# s = [0]
# n = int(input())
# for i in range(n):
#     point = int(input())
#     s.append(point)

# if n == 1:
#     print(s[n])
# else:
#     dp[1][1] = s[1]
#     dp[1][2] = 0
#     dp[2][1] = s[2]
#     dp[2][2] = s[1] + s[2]

#     for i in range(3,n+1):
#         dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + s[i]
#         dp[i][2] = dp[i-1][1] + s[i]

#     print(max(dp[n][1],dp[n][2]))