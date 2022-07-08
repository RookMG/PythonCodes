def solution(land, P, Q):
    left = min(min(_) for _ in land)
    right = min(min(_) for _ in land)
    mid = (left+right)//2
    leftval = 0
    rightval = 0
    for i in land:
        for j in land:
            leftval += P*(leftval-j) if j<leftval else Q*(j-leftval)
            rightval += P*(rightval-j) if j<rightval else Q*(j-rightval)
    while left<right:
        answer = 0
        for i in land:
            for j in i:
                answer += P*(mid-j) if j<mid else Q*(j-mid)
        if 

    return answer
print(max(max(_) for _ in a))