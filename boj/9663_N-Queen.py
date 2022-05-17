'''
https://boj.kr/9663
'''
import sys
input = sys.stdin.readline

n = int(input())
isColumnUsed = [0]*(2*n)     # | column 확인
isLRDiagnoalUsed = [0]*(2*n) # / x+y 값 확인
isRLDiagnoalUsed = [0]*(2*n) # \ x-y 값 확인 (x-y+n-1) <-- 인덱스 음수 방지

cnt = 0
def func(cur): # cur은 row - x좌표 (수학 기준)
    global cnt
    if cur == n:
        cnt += 1
        return
    for i in range(1,n+1): # col - y좌표 (수학 기준)
        if isColumnUsed[i] or isLRDiagnoalUsed[cur+i] or isRLDiagnoalUsed[cur - i + n - 1]:
            continue
        isColumnUsed[i] = True
        isLRDiagnoalUsed[cur+i] = True
        isRLDiagnoalUsed[cur - i + n - 1] = True
        func(cur+1)
        isColumnUsed[i] = False
        isLRDiagnoalUsed[cur+i] = False
        isRLDiagnoalUsed[cur - i + n - 1] = False

func(0)
print(cnt)