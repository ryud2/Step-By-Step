import sys

def Prime(n):
    for i in range(2,int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True 

L ={}

A , B = map(int,sys.stdin.readline().split())
if A == 1 :
    A = 2 
for i in range(A,B+1):
    if Prime(i):
        print(i)