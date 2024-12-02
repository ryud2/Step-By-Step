a , b = map(int,input().split())
c = int(input())
n = int(input())
if a == c :
    print(1 if b <=0 else 0)
elif a < c:
    print(1 if a*n+b <= c*n else 0)
else :
    print(0)