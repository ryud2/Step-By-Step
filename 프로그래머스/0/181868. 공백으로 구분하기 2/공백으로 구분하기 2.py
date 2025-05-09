def solution(my_string):
    my_string = my_string.split(" ")
    while "" in my_string:
        my_string.remove("")
    return my_string