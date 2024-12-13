import sys

while True:
    T = list(sys.stdin.readline())
    L = []
    
    Test = []
    
    if T[0] == ".":
        break
          
    for i in T:
        if i == "(" or i == ")" or i == "[" or i == "]" :
            if i == ")" :
            
                if len(Test) == 0:
                    print("no")
                    break
                
                if Test[-1] != "(":
                    print("no")
                    break
                
                else :
                    Test.pop()
                    continue
                
            elif i == "]" :
                
                if len(Test) == 0:
                    print("no")
                    break
                
                if Test[-1] != "[":
                    print("no")
                    break
                
                else :
                    Test.pop()
                    continue
            
            Test.append(i)
            
    else:
        if len(Test) == 0:
            print("yes")
        else :
            print("no")