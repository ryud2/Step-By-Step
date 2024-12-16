import sys
from collections import deque

N = int(sys.stdin.readline())

Deck = deque()

for i in range(N):
    Command = list(map(int,sys.stdin.readline().split()))
    
    if Command[0] == 1 :
        Deck.appendleft(Command[1])
        
    elif Command[0] == 2 :
        Deck.append(Command[1])
        
    elif Command[0] == 3 :  
        if len(Deck) == 0 :
            print(-1)
        else :
            print(Deck.popleft())
        
    elif Command[0] == 4 :
        if len(Deck) == 0 :
            print(-1)
        else :
            print(Deck.pop())
        
    elif Command[0] == 5 :
        print(len(Deck))
        
    elif Command[0] == 6 :
        if len(Deck) == 0 :
            print(1)
        else :
            print(0)
            
    elif Command[0] == 7 :
        if len(Deck) == 0 :
            print(-1)
        else :
            print(Deck[0])
            
    elif Command[0] == 8 :
        if len(Deck) == 0 :
            print(-1)
        else :
            print(Deck[-1])