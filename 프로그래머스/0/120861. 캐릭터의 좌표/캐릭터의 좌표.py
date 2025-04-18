def solution(keyinput, board):
    location = [0,0]
    for i in keyinput:
        if i == "left":
            location[0] -= 1
        elif i == "right":
            location[0] += 1
        elif i == "down":
            location[1] -= 1
        elif i == "up":
            location[1] += 1
        if location[0] > board[0]//2:
            location[0] = board[0]//2
        if location[0] < - (board[0]//2):
            location[0] = - (board[0]//2)
        if location[1] > board[1]//2:
            location[1] = board[1]//2
        if location[1] < - (board[1]//2):
            location[1] = - (board[1]//2)    

    return location