import sys
input = sys.stdin.readline

nums = [0]*10
n = int(input())

while n:
    cur = n % 10
    if cur == 6 or cur == 9:
        if nums[6] > nums[9]:
            nums[9] += 1
        else:
            nums[6] += 1
    else:
        nums[cur] += 1
    n //= 10

print(max(nums))