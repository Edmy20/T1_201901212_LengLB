#No Idea!; Ejecicio 11


sadness=0
happiness=0
_ = input()
data = input().split()
happy = set(input().split())
sad = set(input().split())

happiness=sum(i in happy for i in data) 
sadness=sum(i in sad for i in data) 
print(happiness-sadness)