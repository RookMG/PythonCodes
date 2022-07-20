def solution(N, number):
    uses = [set() for _ in range(9)]
    for i in range(1,9):
        uses[i].add(int(str(N)*i))
        for j in range(i//2+1):
            for a in uses[j]:
                for b in uses[i-j]:
                    uses[i].update([a+b,a*b,a-b,b-a])
                    if a!=0:
                        uses[i].add(b//a)
                    if b!=0:
                        uses[i].add(a//b)
        if number in uses[i]:
            return i
    return -1