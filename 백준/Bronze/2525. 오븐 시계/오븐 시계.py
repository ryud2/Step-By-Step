h , m  = map(int,input().split())
t = int(input())

time = h*60 + m

print(((time + t ) //60)%24 , ( m + t ) % 60)