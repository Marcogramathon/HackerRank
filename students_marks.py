if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(query_name)
    # print(student_marks[query_name])
    # print(student_marks[query_name][0])
    suma = 0
    for i in student_marks[query_name]:
        suma += i
    prom = suma/(len(student_marks))
    print(suma)
    print(len(student_marks))
    print(format(prom, ".2f"))