import sys

S = sys.stdin.readline().strip()
K = sys.stdin.readline().strip()
A = ""
for i in S:
    try:
        i = int(i)
        pass
    except:
        A += i
        
if K in A:
    print(1)
else:
    print(0)