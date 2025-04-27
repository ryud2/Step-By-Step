def solution(board):
    answer = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                for i in range(-1,2):
                    for j in range(-1,2):
                        try:
                            if board[row+i if row+i >= 0 else row][col+j if col +j >= 0 else col] == 0:
                                board[row+i][col+j] = 2
                        except:
                            pass
    for k in board:
        answer += k.count(0)
    return answer