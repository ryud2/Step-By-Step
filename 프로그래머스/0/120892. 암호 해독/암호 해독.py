def solution(cipher, code):
    answer = ''
    cipher = list(cipher)
    num = -1
    num += code
    while  len(cipher) > num :
        answer +=cipher[num]
        num += code
    
    return answer