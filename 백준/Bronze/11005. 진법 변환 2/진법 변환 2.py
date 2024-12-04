N , B = map(int,input().split())
J =['0', '1','2', '3', '4','5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
A = []
while True :
    Q = N // B
    R = N % B
    N = Q
    A.insert(0 ,J[R])
    if Q == 0:
        break
print(''.join(A))