import sys

S = sys.stdin.readline().strip()

for i in S:
    if i.isupper():
        print(i.lower(), end ="")
    else:
        print(i.upper(), end ="")