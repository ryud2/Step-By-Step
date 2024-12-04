N = int(input())
K = 6
i = 1
if N == 1:
    i = 0
N -=1
while True:
    N = N - K
    K += 6
    i += 1
    if N <= 0:
        break
print(i)