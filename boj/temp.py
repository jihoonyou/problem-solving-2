
def rot_right(board):
    return [list(elem) for elem in list(zip(*board[::-1]))]

def rot_left(board):
    return [list(elem) for elem in list(zip(*board))[::-1]]

board = [0][0]
N = len(board)
def gravity(board):
    for col in range(N):
        for row in range(N-2,-1,-1):
            if board[col][row] != -1: # 움직이지 않는 벽
                r = row
                while True:
                    if r+1 < N and board[r+1][col] == -2: # 빈 공간
                        board[r+1][col],board[r][col] = board[r][col], board[r+1][col]
                        r += 1
                    else:
                        break

# def rot_right(board):
#     row = len(board)
#     col = len(board[0])
#     ret = [[0 for _ in range(row)] for _ in range(col)]

#     for 

def rot_right(board):
    n = len(board)
    ret = [[0 for _ in range(N)] for _ in range(N)]
    for 

# 아까의 단서에서 회전 전의 열과 후의 행이 일치한다고 했다. 따라서 두 곳에는 c 값을 그대로 준다
# 
# ret[c][N-1-r] = m[r][c]

def rotate(tgt_list, angle):
    n = len(tgt_list)
    m = len(tgt_list[0])
    if angle == 1:
        result = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                result[j][n - i - 1] = tgt_list[i][j]
        return result
    elif angle == 2:
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                result[n - i - 1][m - j - 1] = tgt_list[i][j]
        return result
    elif angle == 3:
        result = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                result[m - j - 1][i] = tgt_list[i][j]
        return result
    else:
        return tgt_list