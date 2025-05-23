def solution(board, k):
    answer = 0
    for i in range(k+1):
        for j in range(k-i+1):
            try :
                answer += board[i][j] 
            except :
                pass
    return answer