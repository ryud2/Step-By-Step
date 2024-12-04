import sys
N = [int(input()) for i in range(9)]
Max = 0
for i in range(len(N)):
    if Max < int(N[i]) :
        Max = N[i]
        number = i+1
print(Max)
print(number)