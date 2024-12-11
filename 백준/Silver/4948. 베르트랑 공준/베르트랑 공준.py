import sys

def Prime(n):
    for i in range(2,int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True 


while True:
    C = 0
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    for i in range(n+1,2*n+1):
        if Prime(i):
            C += 1
    print(C)
    