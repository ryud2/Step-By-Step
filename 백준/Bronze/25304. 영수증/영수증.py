total = int(input())
number = int(input())
sum = 0
for i in range(number):
    price , count = map(int,input().split())
    sum += price * count
if total == sum :
    print("Yes")
else : 
    print("No")