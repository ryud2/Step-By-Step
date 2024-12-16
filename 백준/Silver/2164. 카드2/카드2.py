import sys
from collections import deque

card = deque( i for i in range(1 ,int(sys.stdin.readline())+1))


while len(card) >= 2:
    card.popleft()
    card.append(card.popleft())

print(card[0])