def solution(rows, columns, lands):
    sizes = []
    map = [[0 for w in range(columns)] for l in range(rows)]
    for i, j in lands:
        map[i-1][j-1] = 1
    for i in range(rows):
        for j in range(columns):
            if map[i][j] == 0:
                map,size = findSize(map,0,i,j)
                if max(i,j)>0:
                    sizes.append(size)
                
                for _ in map:
                    print(_)
                print(size)
                print()
    answer = [min(sizes),max(sizes)] if len(sizes) > 0 else [-1,-1]
    return answer

def findSize(map,size,i,j):
    map[i][j] = 2
    size+=1
    if i>0:
        if map[i-1][j] == 0:
            map, size = findSize(map,size,i-1,j)
    if j>0:
        if map[i][j-1] == 0:
            map, size = findSize(map,size,i,j-1)
    if i<len(map)-1:
        if map[i+1][j] == 0:
            map, size = findSize(map,size,i+1,j)
    if j<len(map[0])-1:
        if map[i][j+1] == 0:
            map, size = findSize(map,size,i,j+1)
    return map, size
solution(9,7,[[2, 2], [2, 3], [2, 5], [3, 2], [3, 4], [3, 5], [3, 6], [4, 3], [4, 6], [5, 2], [5, 5], [6, 2], [6, 3], [6, 4], [6, 6], [7, 2], [7, 6], [8, 3], [8, 4], [8, 5]])