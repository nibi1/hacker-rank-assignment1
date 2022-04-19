if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        ls = input().split()
        name = ls[0]
        del ls[0]
        scores = [float(i) for i in ls]
        student_marks[name] = scores
    qn = input()
    qs = student_marks[qn]
    s = sum(qs)/len(qs)
    print("{0:.2f}".format(s))
