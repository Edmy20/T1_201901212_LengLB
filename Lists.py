#Lists; Ejercicio 10

if __name__ == '__main__'
    list=[]
    N = int(input())
    for i in range(N)
        a=input()
        action=a.split()
        if len(action)==3
            list.insert(int(action[1]),int(action[2]))
        elif len(action)==2 and action[0]==append
            list.append(int(action[1]))
        elif len(action)==2 and action[0]==remove
            list.remove(int(action[1]))
        elif a==print
            print(list)
        elif a==sort
            list.sort()
        elif a==pop
            list.pop()
        elif a==reverse
            list.reverse()
