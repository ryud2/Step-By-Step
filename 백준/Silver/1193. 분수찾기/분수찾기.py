X = int(input())
i = 0
while True:
    X -= i
    if X <= i + 1:
        break
    i += 1
if i %2 == 1 :
    print("{0}/{1}".format(X,i+2-X))
else :

    print("{0}/{1}".format(i+2-X,X))