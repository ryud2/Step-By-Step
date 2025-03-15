def solution(my_string):
    S = 0
    for i in my_string:
        try :
            i = int(i)
            S += i
        except:
            pass
        
    return S