def solution(triangle):
    add = [0]*len(triangle[-1])
    for line in reversed(triangle):
        line = [i+j for i,j in zip(line,add)]
        add=[]
        if len(line)==1:
            return line[0]
        else:
            for _ in range(len(line)-1):
                add.append(max(line[_],line[_+1]))

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))