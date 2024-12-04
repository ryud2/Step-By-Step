A = [int(input()) for i in range(5)]
A.sort()
print("{0}\n{1}".format(sum(A)//5,A[2]))