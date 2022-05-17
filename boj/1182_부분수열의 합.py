'''
https://boj.kr/1182
'''
import sys
input = sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
def func(cur, total): # 여기서 cur 은 역시나 숫자들을 선택 또는 안하는 index
    global cnt
    if cur == n: # 선택하고 안하고를 주어진 부분수열의 개수만큼 했을 때
        if total == s:
            cnt += 1
        return
    func(cur+1, total)
    func(cur+1, total + arr[cur])

func(0,0)

if s == 0: # 크기가 양수인 부분수열 중 (공집합 제거)
    cnt -= 1

print(cnt)