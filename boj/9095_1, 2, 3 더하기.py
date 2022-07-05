import sys
input = sys.stdin.readline

def backtracking(_sum, n):
    global count
    if _sum == n:
        count += 1
        return
    if _sum > n:
        return
    for i in range(1,4):
        backtracking(_sum+i,n)

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    backtracking(0,n)
    print(count)

# dp = [0]*11
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4

# for i in range(4,len(dp)):
#     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# for _ in range(t):
#     n = int(input())
#     print(dp[n])
