def solution(strs, t):
    answer = bfs(strs,t,1)
    return answer

def bfs(strs,t,depth):
    t=1
    test = ['' for _ in strs]
    while t<=depth:
        for _ in range(len(strs)):
            if strs[_] == t:
                return t
            elif test[_]+strs[_] == t[:len(strs[_])]:
                test[_] += strs[_]
    if depth<len(t):
        return bfs(strs,t,depth+1)
    else:
        return -1
print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))