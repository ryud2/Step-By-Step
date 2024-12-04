Text = list(input())
for i in range(len(Text)//2):
    if Text[i] != Text[-(i+1)]:
        print("0")
        break    
    if abs(i) == abs(len(Text)//2-1):
        print("1")
        break
if len(Text) == 1:
    print("1")