A = int(input())
for i in range(1,A+1):
    print(" "*(A-i) + "*"*(i*2-1))
for i in range(A-1 , 0 , -1):
    print(" "*(A-i) + "*"*(i*2-1))