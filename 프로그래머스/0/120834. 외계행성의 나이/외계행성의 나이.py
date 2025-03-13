def solution(age):
    C = ["a","b","c","d","e","f","g","h","i","j"]
    Answer = ""
    for i in list(map(int,str(age))):
        Answer += C[i]
    return Answer