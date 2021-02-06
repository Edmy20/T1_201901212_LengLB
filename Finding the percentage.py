#Finding the percentage; Ejercicio 9


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
grades=0

for i in student_marks[query_name]:
    grades+=i

avarage=grades/3

print('%.2f'% avarage)