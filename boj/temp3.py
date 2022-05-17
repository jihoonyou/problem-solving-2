from termios import N_TTY


def rotate_right(board):
    return [list(elem) for elem in list(zip(*board[::-1]))]

def rotate_left(board):
    return [list(elem) for elem in list(zip(*board))[::-1]]


def rot_print(board):
    for rr in board:
        print(*rr)
    print('-------------------')

board = [[1,2,3],[4,5,6],[7,8,9]]

board2 = [[1,2,3],[-2,-1,2],[-2,-2,-1]]

rot_print(board)

r_board = rotate_right(board)

l_board = rotate_left(board)

rot_print(r_board)
rot_print(l_board)

def gravity(board): # 벽 -1, 빈공간 -2라면
    for col in range(len(board[0])):
        for row in range(len(board)-2,-1,-1):
            if board[row][col] != -1:
                r = row
                while True:
                    if r + 1 < len(board) and board[r+1][col] == -2:
                        board[r][col],board[r+1][col] = board[r+1][col], board[r][col]
                        r += 1
                    else:
                        break
rot_print(board2)
gravity(board2)

rot_print(board2)

max_eat = -1
eat = list()
temp = [[]]
def shark_move(y,x,cur,cnt,visited):
    global max_eat, eat
    if cur == 3:
        if max_eat < cnt:
            max_eat = cnt
            eat = visited[:]
        return
    for dy,dx in dr:
        ny = dy + y
        nx = dx + x
        if 0 <= ny <4 and 0 <= nx < 4:
            if (ny,nx) not in visited:
                visited.append((ny,nx))
                shark_move(ny,nx,cur+1, cnt + len(temp[ny][nx]), visited)
                visited.pop((ny,nx))
            else:
                shark_move(ny,nx,cur+1, cnt, visited)