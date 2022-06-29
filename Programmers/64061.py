def solution(board, moves):
    answer = 0
    out = []
    depth = len(board)
    for move in moves:
        floor = 0
        kind = 0
        while floor<depth:
            kind = board[floor][move-1]
            if kind != 0 :
                board[floor][move-1]=0
                out.append(kind)
                if len(out)>1:
                    if out[-1]==out[-2]:
                        answer+=2
                        out = out[:-2]
                break
            floor += 1
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))