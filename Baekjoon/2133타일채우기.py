from collections import deque

def solution(n, path, order):
    answer = True
    links = {n: [] for n in range(n)}
    for i, j in path:
        links[i].append(j)
        links[j].append(i)
    left, right = {},{}
    for a, b in order:
        left[a] = b
        right[b] = a
        if b == 0:
            return False
        if a == 0:
            left[0] = 0
    visit = [0]*n
    visit[0] = 1
    q = deque()
    q.append(0)
    while q:
        pos = q.popleft()
        if pos == left.get(right.get(pos)):
            visit[pos] = 2
        else:
            for link in links[pos]:
                if visit[link] == 0:
                    q.append(link)
                    visit[link] = 1
                    if left.get(link):
                        if visit[left[link]] == 2:
                            q.append(left[link])
                            visit[left[link]] = 1
                        left[link] = 0
    return False if 0 in visit else answer