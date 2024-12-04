Text = list(input())
Len = []
M = 0
C = []
for i in range(len(Text)):
    if ord(Text[i]) >= 97 :
        Text[i] = chr(ord(Text[i]) - 32)
    Len.append(Text[i])
for x in list(set(Len)):
    if M < Len.count(x):
        M = Len.count(x)
        C = [x]
    elif M == Len.count(x):
        C.append(x)
if len(C) >= 2:
    print("?")
else :
    print(*C)