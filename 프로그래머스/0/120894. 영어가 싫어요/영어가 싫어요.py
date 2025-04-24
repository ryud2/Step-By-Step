def solution(numbers):
    answer = ""
    while numbers != "":
        if numbers[0:3] == "one":
            answer += "1"
            numbers = numbers[3:]

        elif numbers[0:3] == "two":
            answer += "2"
            numbers = numbers[3:]

        elif numbers[0:5] == "three":
            answer += "3"
            numbers = numbers[5:]

        elif numbers[0:4] == "four":
            answer += "4"
            numbers = numbers[4:]

        elif numbers[0:4] == "five":
            answer += "5"
            numbers = numbers[4:]

        elif numbers[0:3] == "six":
            answer += "6"
            numbers = numbers[3:]

        elif numbers[0:5] == "seven":
            answer += "7"
            numbers = numbers[5:]

        elif numbers[0:5] == "eight":
            answer += "8"
            numbers = numbers[5:]

        elif numbers[0:4] == "nine":
            answer += "9" 
            numbers = numbers[4:]

        elif numbers[0:4] == "zero":
            answer += "0"
            numbers = numbers[4:]
    return int(answer)