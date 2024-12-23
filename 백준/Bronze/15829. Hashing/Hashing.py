import sys

Alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

L = int(sys.stdin.readline())

String = sys.stdin.readline().strip()

Sum = 0

for i in range(L):
    Sum += (Alpha.index(String[i]) + 1) * 31**i
    
print(Sum %1234567891)