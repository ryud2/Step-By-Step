cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]
T =input()
for i in cro:
    T = T.replace(i,"*")
print(len(T))