import sys
import functools

T = int(sys.stdin.readline())

@functools.cache
def fi(x):
    
    if x == 0:
        a1 , b1 = 1 , 0
        return [a1,b1]
    elif x == 1:
        a2 , b2 = 0 , 1
        return [a2,b2]
    else:
        sum = [x+y for x,y in zip(fi(x-1) , fi(x-2))]
        return sum
    
for i in range(T):
    print(*fi(int(sys.stdin.readline())))