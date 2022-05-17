'''
https://boj.kr/1780
참고
https://tmdrl5779.tistory.com/103
https://st-lab.tistory.com/235
'''
import sys
input = sys.stdin.readline

N = int(input())

paper = []
for _ in range(N):
    row = list(map(int,input().split()))
    paper.append(row)

res = [0,0,0]

def color_check(y,x,n):
    check = paper[y][x]
    for r in range(y,y + n):
        for c in range(x,x + n):
            if paper[r][c] != check:
                return False
    return True

def paper_cut(y,x,n):
    if color_check(y,x,n):
        check = paper[y][x]
        if check == -1:
            res[0] += 1
        elif check == 0:
            res[1] += 1
        else: 
            res[2]  += 1
        return

    n = n // 3
    paper_cut(y,x,n)
    paper_cut(y,x + n,n)
    paper_cut(y,x + 2*n,n)

    paper_cut(y + n,x,n)
    paper_cut(y + n,x + n,n)
    paper_cut(y + n,x + 2*n,n)

    paper_cut(y + n*2,x,n)
    paper_cut(y + n*2,x + n,n)
    paper_cut(y + n*2,x + 2*n,n)

paper_cut(0,0,N)
for answer in res:
    print(answer)

'''
import sys
input = sys.stdin.readline

N = int(input())

paper = []
for _ in range(N):
    row = list(map(int,input().split()))
    paper.append(row)

res = [0,0,0]

def paper_cut(y,x,n):
    check = paper[y][x]
    for r in range(y,y + n):
        for c in range(x,x + n):
            if paper[r][c] != check:
                check = -2
                break

    if check == -2:
        n = n // 3
        paper_cut(y,x,n)
        paper_cut(y,x + n,n)
        paper_cut(y,x + 2*n,n)
        paper_cut(y + n,x,n)
        paper_cut(y + n,x + n,n)
        paper_cut(y + n,x + 2*n,n)
        paper_cut(y + n*2,x,n)
        paper_cut(y + n*2,x + n,n)
        paper_cut(y + n*2,x + 2*n,n)
    elif check == -1:
        res[0] += 1
    elif check == 0:
        res[1] += 1
    else: 
        res[2]  += 1
paper_cut(0,0,N)
for answer in res:
    print(answer)
'''