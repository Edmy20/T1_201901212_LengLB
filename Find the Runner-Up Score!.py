#Find the Runner-Up Score!; Ejercicio 8

if __name__=='__main__':
  n = int(input())
  arr=map(int, input().split())
  num=list(arr)
  
for _ in range(n):
    for i in range (n-1):
        if num[i]>=num[i+1]:
            a=num[i]
            num[i]=num[i+1]
            num[i+1]=a
            
res=[]
for j in num:
 if j not in res:
    res.append(j)
    
r=len(res)-2

print(res[r])