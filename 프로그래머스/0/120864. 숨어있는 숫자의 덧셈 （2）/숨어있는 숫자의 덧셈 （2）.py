def solution(my_string):
    answer = 0
    while my_string != "":
        if my_string[0:4].isdigit() and len(my_string) >= 4: 
            answer += int(my_string[0:4])
            my_string = int(my_string[4:])
        elif my_string[0:3].isdigit() and len(my_string) >= 3:
            answer += int(my_string[0:3])
            my_string = my_string[3:]
        elif my_string[0:2].isdigit() and len(my_string) >= 2:
            answer += int(my_string[0:2])
            my_string = my_string[2:]
        elif my_string[0].isdigit() :
            answer += int(my_string[0])
            my_string = my_string[1:]
        else:
            my_string = my_string[1:]
    return answer