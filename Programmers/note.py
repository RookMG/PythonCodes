def solution(n):
    sets = [set() for _ in range(15)]
    sets[1].add('()')
    for i in range(2,n+1):
        for j in range(i//2+1):
            sets[i].add(sets[j]+sets[i-j])
            sets[i].add(sets[i-j]+sets[j])
        for shorts in sets[i-1]:
            sets[i].update((shorts+"()","("+shorts+")","()"+shorts))
    return len(sets[n])
print(solution(4))