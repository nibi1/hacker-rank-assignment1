if __name__ == '__main__':
    student_marksheet = []
    scoresheet = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        student_marksheet +=[[name, score]]
        scoresheet += [score]
    x = sorted(set(scoresheet))[1]
    
    for n, s in sorted(student_marksheet):
        if s == x:
            print(n)
