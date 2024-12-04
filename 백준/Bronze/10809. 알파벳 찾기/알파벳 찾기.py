alpha = [chr(c) for c in range(ord('a'),ord('z')+1)]
word = input()
for i in range(26) :
    print(word.find(alpha[i]) , end =' ')