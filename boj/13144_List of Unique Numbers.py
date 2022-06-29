import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

en = 0
visit = [0]*(n+1)
visit[nums[en]] = 1
res = 0
for st in range(n):
    while en < n - 1 and not visit[nums[en+1]]:
        en+=1
        visit[nums[en]] = 1

    res += en - st + 1
    visit[nums[st]] = 0
print(res)
