from collections import deque
m,n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

q = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            dist[i][j] = 0
            q.append((i,j))

def bfs() :
    while q :
        r,c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 > nr or n <= nr or 0 > nc or m <= nc or grid[nr][nc] == -1:
                continue
            if grid[nr][nc] == 0 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr,nc))
            
bfs()
check = False
max_dist = -1
for i in range(n) :
    for j in range(m) :
        if grid[i][j] != -1 and dist[i][j] == -1 :
            check = True
            break
        max_dist = max(max_dist, dist[i][j])
if check :
    print(-1)
else :
    print(max_dist)