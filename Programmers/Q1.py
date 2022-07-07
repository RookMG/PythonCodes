def solution(grade):
    answer = 0
    l = len(grade)-1
    for _ in range(l):
        if grade[l-_]<grade[l-_-1]:
            answer += grade[l-_-1] - grade[l-_]
            grade[l-_-1] = grade[l-_]
    return answer