import sys

n = sys.stdin.readline()

S = sys.stdin.readline().strip()

S = S.replace("I","i")
S = S.replace("l","L")

print(S)