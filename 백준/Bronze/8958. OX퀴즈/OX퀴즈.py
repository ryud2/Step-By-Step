import sys

for i in range(int(sys.stdin.readline())):
    
    combo = 0
    score = 0
    for j in list(sys.stdin.readline().strip()):
        if j == "O" :
            combo += 1
        if j == "X":
            combo = 0
            
        score += combo
        
    print(score)