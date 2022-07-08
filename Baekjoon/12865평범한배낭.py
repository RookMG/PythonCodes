n, maxweight = map(int, input().split())
data = []
best = [[0]*(maxweight+1) for _ in range(n)]
for _ in range(n):
    data.append(input())
for i in range(n):
    w, v = map(int,data[i].split())
    for j in range(maxweight+1):
        if j>=w:
            best[i][j] = max(v if i==0 else v+best[i-1][j-w],0 if i == 0 else best[i-1][j])
        elif i>0:
            best[i][j] = best[i-1][j]
print(best)
print(best[-1][-1])