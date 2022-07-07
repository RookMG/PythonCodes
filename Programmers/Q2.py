def solution(n, horizontal):
    answer = [[0 for w in range(n)] for l in range(n)]
    way = [-1,1]
    way.append(1 if horizontal is True else -1)
    for i in range(n):
        for j in range(n):
            if i==j:
                answer[i][j] = i*i+i+1
            elif i>j:
                answer[i][j] = (i*i+i+1)+way[2]*way[i%2]*(i-j)
            else:
                answer[i][j] = (j*j+j+1)+way[2]*way[j%2]*(i-j)
    return answer

print(solution(5,0))