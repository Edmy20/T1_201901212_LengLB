#Word Order; Ejercicio 12

if __name__ == '__main__':
    n = int(input())
    w={}
    appear=[]

    for i in range(n):
        word=input()
        appear.append(word)


for item in appear:
    n=0
    if item not in w:
        w[item]=1
    else:
        w[item]+=1
        
print(len(w))
for i in w:
    print(w[i], end=" ")