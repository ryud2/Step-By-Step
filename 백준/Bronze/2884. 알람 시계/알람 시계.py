h , m = map(int,input().split())
if h == 0 :
    h = h +24

if m >= 45 :
    m = m - 45
else :
    m = m + 15
    h = h - 1

if h == 24 : 
    h = 0
print(h , m)