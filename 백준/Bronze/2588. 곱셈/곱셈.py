first = int(input())
second = int(input())

second_hun = second//100
second_ten = (second - second_hun*100)//10
second_one = second - second_hun*100 - second_ten*10

print(second_one*first)
print(second_ten*first)
print(second_hun*first)
print(second*first)
