import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
stack = []
ans = [-1]*n

for i in range(len(nums)):
    num = nums[i]
    while stack:
        pre_num,index = stack[-1]
        if pre_num < num:
            ans[index] = num
            stack.pop()
        else:
            break
    stack.append((num,i))
print(' '.join(map(str,ans)))