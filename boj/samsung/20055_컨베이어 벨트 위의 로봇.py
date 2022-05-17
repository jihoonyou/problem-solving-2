'''
https://boj.kr/20055
'''
import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
belt = deque(map(int,input().split()))
robot = deque([False]*N)
res = 0

while True:
    res += 1
    # step 1
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = False

    # step 2
    for i in range(N-2,-1,-1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i] = False
            robot[i+1] = True
            belt[i+1] -= 1
    robot[-1] = False

    # step 3
    if belt[0] > 0 and not robot[0]:
        belt[0] -= 1
        robot[0] = True

    if belt.count(0) >= K:
        break
print(res)