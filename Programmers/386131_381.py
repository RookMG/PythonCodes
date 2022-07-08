def solution(land, P, Q):
    left = min(min(_) for _ in land)
    right = max(max(_) for _ in land)
    answer = (right-left)*len(land)*len(land[0])*max(P,Q)
    for _ in range(right-left):
        temp = 0
        for i in land:
            for j in i:
                temp += P*(_+left-j) if j<_+left else Q*(j-_-left)
        answer = min(answer,temp)
    return answer
print(min(min(_) for _ in [[4, 4, 3], [3, 2, 2], [ 2, 10, 9 ]]))