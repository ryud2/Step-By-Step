N = input()
Check = 0
Lo = 0
for i in range(0,12):
    if N[i] != "*":
        Check += int(N[i])*(1 if i%2 == 0 else 3)
    else:
        Lo = i

for j in range(10):
    if ((j*(1 if Lo%2 == 0 else 3) + Check + int(N[-1]))%10 )== 0:
        print(j)