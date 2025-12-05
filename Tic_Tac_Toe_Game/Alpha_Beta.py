import os, math

#kiểm tra trường hợp thắng trên bàn cơ
def GetWinner(board):
    if board[0] == board[1] and board[1] == board[2]:
        return board[0]
    elif board[3] == board[4] and board[4] == board[5]:
        return board[3]
    elif board[6] == board[7] and board[7] == board[8]:
        return board[6]
    elif board[0] == board[3] and board[3] == board[6]:
        return board[0]
    elif board[1] == board[4] and board[4] == board[7]:
        return board[1]
    elif board[2] == board[5] and board[5] == board[8]:
        return board[2]
    elif board[0] == board[4] and board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] and board[4] == board[6]:
        return board[2]
    
def PrintBoard(board):
    os.system('cls' if os.name=='nt' else 'clear')
    print(f'''
          {board[0]}|{board[1]}|{board[2]}
          {board[3]}|{board[4]}|{board[5]}
          {board[6]}|{board[7]}|{board[8]}
          ''')

#tìm các ô còn trống trên bàn cờ    
def GetAvailableCells(board):
    available = list()
    for cell in board:
        if cell !="X" and cell !="O":
            available.append(cell)
    return available

def minimax(position, depth, alpha, beta, isMaximizing):
    #điều kiện dừng
    winner = GetWinner(position)
    if winner != None:
        return 10 -depth if winner =="X" else -10 +depth
    if len(GetAvailableCells(position))==0:
        return 0
    #người chơi Max
    #tìm nước đi cho điểm cao và cập nhật alpha
    if isMaximizing:
        maxEval = -math.inf
        for cell in GetAvailableCells(position):
            position[cell-1]="X"
            Eval=minimax(position,depth+1, alpha, beta, False)
            maxEval = max(maxEval, Eval)
            alpha = max(alpha, Eval)
            position[cell-1]=cell
            if beta <= alpha:
                break
        return maxEval
    else: #người chơi Min, tìm nước đi thấp điểm và cập nhật beta 
        minEval = +math.inf
        for cell in GetAvailableCells(position):
            position[cell-1]="O"
            Eval = minimax(position, depth +1, alpha, beta, True)
            minEval = min(beta, Eval)
            beta = min(beta, Eval)
            position[cell -1 ]=cell
            if beta <= alpha:
                break
        return minEval
    
#tìm nước đi tốt nhất cho AI    
def FindBestMove(currentPosition, AI): 
    bestVal = -math.inf if AI =="X" else +math.inf
    bestMove = -1
    for cell in GetAvailableCells(currentPosition):
        currentPosition[cell -1]=AI
        moveVal=minimax(currentPosition, 0, -math.inf, +math.inf, False if AI == "X" else True)
        currentPosition[cell -1]=cell
        if AI =="X" and moveVal >bestVal:
            bestMove=cell
            bestVal=moveVal
        elif AI=="O" and moveVal < bestVal:
            bestMove = cell
            bestVal = moveVal
    return bestMove

def main():
    player=input("Play as X or O?").strip().upper()
    AI="O" if player =="X" else "X"
    currentGame = [*range(1,10)]
    currentTurn = "X"
    counter = 0
    while True:
        if currentTurn==AI:
            cell = FindBestMove(currentGame, AI)
            currentGame[cell-1]=AI
            currentTurn=player
        elif currentTurn == player:
            PrintBoard(currentGame)
            while True:
                humanInput = int(input("Enter Number:").strip())
                if humanInput in currentGame:
                    currentGame[humanInput-1]=player
                    currentTurn = AI
                    break
                else:
                    PrintBoard(currentGame)
                    print("Cell Not Available.")
            if GetWinner(currentGame) !=None:
                PrintBoard(currentGame)
                print(f"{GetWinner(currentGame)} WON!!")
                break
            counter +=1
            if GetWinner(currentGame) == None and counter==9:
                PrintBoard(currentGame)
                print("Tie.")
                break

if __name__=="__main__":
    main()
