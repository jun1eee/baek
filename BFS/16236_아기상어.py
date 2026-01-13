from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

size = 2
ate = 0
time = 0

for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 9 :
            r, c = i, j
            arr[i][j] = 0

def bfs() :
    visited = [[False] * n for _ in range(n)]
    q = deque([(r, c, 0)])
    # q.append((r, c, 0))
    visited[r][c] = True 
    
    can_eat = []
    
    while q :
        cr, cc, dist = q.popleft()
        for dr, dc in dirs :
            nr, nc = cr + dr, cc + dc
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                if arr[nr][nc] <= size :
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
                    if 0 < arr[nr][nc] < size :
                        can_eat.append((dist + 1, nr, nc))
    if can_eat :
        can_eat.sort()
        return can_eat[0]
    return None 

while True :
    result = bfs()
    if not result :
        break
    dist, rr, cc = result
    time += dist
    r, c = rr, cc
    arr[r][c] = 0
    ate += 1
    
    if ate == size :
        size += 1
        ate = 0
print(time)             