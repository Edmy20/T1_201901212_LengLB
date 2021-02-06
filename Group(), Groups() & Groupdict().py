#Group(), Groups() & Groupdict(); Ejercicio 13



import re

word=input()

m=re.findall("\w",word)
res=""

for i,caracter in enumerate(m):
    if i==0:
        pass
    elif m[i-1]==m[i] and m[i]!="_":
            res=caracter
            break
    else:
        res=-1


print(res)