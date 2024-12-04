A = input().split()
B = input().split()
C = input().split()
print(C[0] if A[0] == B[0] else(B[0] if A[0] == C[0] else A[0]) ,C[1] if A[1] == B[1] else(B[1] if A[1] == C[1] else A[1]))