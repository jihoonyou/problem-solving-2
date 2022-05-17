'''
https://boj.kr/9012
'''
import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    parentheses = input().rstrip()
    counter = 0
    for parnthesis in parentheses:
        if parnthesis == '(':
            counter += 1
        else:
            counter -= 1
            if counter < 0:
                break
    if counter == 0:
        print("YES")
    else:
        print("NO")
 