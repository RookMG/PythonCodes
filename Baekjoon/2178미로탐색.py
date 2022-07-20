import sys
from collections import deque
input = sys.stdin.readline

def move():
    while go:
        i,j = go.pop()
        if i==n-1 and j==m-1:
            return False
        for di, dj in vector:
            ni = i+di
            nj = j+dj
            if 0<=ni<n and 0<=nj<m and visit[ni][nj]==0 and map[ni][nj]=='1':
                next.append([ni,nj])
                visit[ni][nj]=1
    return True

vector = [[1,0],[-1,0],[0,1],[0,-1]]
n, m = map(int,input().split())
map = []
visit = [[0]*m for _ in range(n)]
for _ in range(n):
    map.append(list(input().strip()))
count = 1
go,next = deque(),deque()
go.append([0,0])
visit[0][0]=1
while move():
    go = next
    next = deque()
    count+=1
print(count)