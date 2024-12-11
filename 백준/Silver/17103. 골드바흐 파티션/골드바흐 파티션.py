import sys    

def Prime(n):
    for i in range(2,int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True 

T = int(sys.stdin.readline())

P = {}
A = 2
B = 0

for i in range(T):
    c = 0
    n = int(sys.stdin.readline())
    if n > B:
        B = n
        for j in range(A,B):
            if Prime(j):
                P[j] = 0
    A = B
    P = dict.fromkeys(P,0)
    for k in P:
        if (n-k) in P:
            c +=1
    print(c//2 + c%2)