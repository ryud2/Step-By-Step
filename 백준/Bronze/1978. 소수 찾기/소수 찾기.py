n = int(input())
K = input().split()
C = 0
for S in K:
    S = int(S)
    A = [i for i in range(1,S+1) if S % int(i) == 0]
    if len(A) == 2 :
        C +=1
print(C) 