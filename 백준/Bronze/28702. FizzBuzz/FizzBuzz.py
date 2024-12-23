import sys

S = 0

for i in range(3):
    try :
        S = int(sys.stdin.readline().strip())
        k = S+3-i
        
    except:
        pass

if k % 3 == 0:
    if k % 5 == 0 :
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if k % 5 == 0 :
        print("Buzz")
    else:
        print(k)