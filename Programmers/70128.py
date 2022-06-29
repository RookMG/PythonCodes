def solution(a, b):
    answer = 0
    for _ in range(len(a)):
        answer += a[_]*b[_]
    return answer