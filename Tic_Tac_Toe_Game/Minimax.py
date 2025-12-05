import copy
import math
import random
import numpy

X="X"
O="O"
EMPTY=None
user=None
ai=None

#khởi tạo trạng thái ban đầu cho trò caro
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

#hàm xác định người chơi tiếp theo
#count là hàm đếm tổng số quân trên bàn cờ
#nếu số quân là chẵn thì user đi (hàm này mặc định user bắt đầu trước)
#và nếu số quân là lẻ thì ai đi
def player(board):
    count = 0
    for i in board:
        for j in i:
            if j:
                count +=1
    if count % 2 !=0:
        return ai # nếu lẻ -> AI đi tiếp
    return user # nếu chẵn -> người chơi đi tiếp

 #hàm liệt kê tất cả các nước đi trống/ hợp lệ   
def actions(board):
    res = set() #tạo một tập hợp rỗng lưu các nước đi hợp lệ
    #lấy kích thước bàn cờ,  sau đó duyệt từng hàng và cột
    board_len=len(board)
    for i in range(board_len):
        for j in range(board_len):
            #kiểm tra xem ô đang xét có trống hay không?
            #nếu trống thì thêm tọa độ [i][j] vào tập hợp res
            if board[i][j]==EMPTY:
                res.add((i,j))
    return res

#tạo một bản sao mới và thử các nước đi
def result(board, action):
    curr_player = player(board)
    result_board=copy.deepcopy(board)# tạo một bản sao của bàn cờ
    (i,j) = action
    result_board[i][j]= curr_player
    return result_board

#tìm người thắng theo hàng ngang
def get_horizontal_winner(board):
    winner_val = None
    board_len = len(board)
    for i in range(board_len):
        winner_val= board[i][0]
        if winner_val == ' ' or winner_val is None:
            continue
        for j in range(board_len):
            if board[i][j] !=winner_val:
                winner_val=None
        if winner_val:
            return winner_val
    return winner_val

#tìm người thắng theo hàng dọc    
def get_vertical_winner(board):
    winner_val=None
    board_len=len(board)
    for i in range(board_len):
        winner_val=board[0][i]
        for j in range(board_len):
            if board[j][i] != winner_val:
                winner_val = None
        if winner_val:
            return winner_val
    return winner_val

#tìm người thắng theo đường chéo    
def get_diagonal_winner(board):
    winner_val = None
    board_len = len(board)
    winner_val = board[0][0]#đường chéo chính
    for i in range(board_len):
        if board[i][i] != winner_val:
            winner_val = None
    if winner_val:
        return winner_val
    winner_val = board[0][board_len-1]#đường chéo phụ
    for i in range(board_len):
        j=board_len-1-i
        if board[i][j] !=winner_val:
            winner_val = None
    return winner_val

def winner(board):
    winner_val = get_horizontal_winner(board) or get_vertical_winner(board) or get_diagonal_winner(board) or None
    return winner_val

#hàm kiểm tra trò chơi đã kết thúc chưa
def terminal(board):
    if winner(board) != None:
        return True
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True

#hàm tính điểm 
def utility (board):
    winner_val = winner(board)
    if winner_val == X:
        return 1
    elif winner_val ==0:
        return -1
    return 0


def maxValue(state):
    if terminal(state):
        return utility(state)
    v= -math.inf
    for action in actions(state):
        v = max(v, minValue(result(state, action)))
    return v

def minValue(state):
    if terminal(state):
        return utility(state)
    v= math.inf
    for action in actions(state):
        v=max(v, maxValue(result(state, action)))
    return v

def minimax(board):
    current_player = player(board)
    if current_player == X:
        min_score = -math.inf
        for action in actions(board):
            check= minValue(result(board, action))
            if check > min_score:
                min_score=check
                move = action
    else:
        max_score= math.inf
        for action in actions(board):
            check= maxValue(result(board, action))
            if check < max_score:
                max_score = check
                move = action
    return move

if __name__=="__main__":
    board = initial_state()
    ai_turn = False
    print("Choose  player")
    user = input()
    if user == "X":
        ai = "O"
    else:
        ai = "X"
    while True:
        game_over = terminal(board)
        playr = player(board)
        if game_over:
            winner= winner(board)
            if winner is None:
                print("Game Over: Tie")
            else:
                print(f"Game Over: {winner} wins.")
            break
        else:
            if user !=playr and not game_over:
                if ai_turn:
                    move = minimax(board)
                    board= result(board,move)
                    ai_turn = False
                    print(numpy.array(board))
                elif user == playr and not game_over:
                    ai_turn = True
                    print("Enter the position to move (row,col)")
                    i = int(input("Row:"))
                    j = int(input("Col:"))
                    if board[i][j] == EMPTY:
                        board = result(board, (i,j))
                        print(numpy.array(board))
