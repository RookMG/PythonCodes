def solution(absolutes, signs):
    answer = 0
    for _ in range(len(signs)):
        answer += absolutes[_] if signs[_]==True else -absolutes[_]
    return answer