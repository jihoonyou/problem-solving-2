'''
https://boj.kr/1783
'''
import sys
input = sys.stdin.readline

Y,X = map(int,input().split())

if Y == 1:
    print(1)
elif Y == 2:
    print(min(4,(X-1) // 2 + 1)) # 4는 최소 3번 움직일 수 있는것 + 1 || 시작이 무조건 1 더해지고, 3칸부터 2칸씩 가므로 
elif X <= 6: # Y >= 3 부터는 다 사용 가능 여기서는 X의 제약만 존재
    print(min(4,X))
else:
    print(X-2)
