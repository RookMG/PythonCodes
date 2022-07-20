def solution(X, Y):
    xl ,yl = [0]*10,[0]*10
    for _ in range(10):
        for i in X:
            if int(i) == _:
                xl[_]+=1
        for j in Y:
            if int(j) == _:
                yl[_]+=1
    xl[0] = 1 if xl[0]>0 else 0
    yl[0] = 1 if yl[0]>0 else 0
    answer = ''
    for _ in range(10):
        answer += str(9-_)*min(xl[9-_],yl[9-_])
    if answer == '':
        answer = "-1"
    return answer

solution("100","1243039")