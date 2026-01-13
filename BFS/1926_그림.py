from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(i, j) :
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    size = 1
    while q :
        r, c = q.popleft()
        for dr, dc in dirs :
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m :
                continue
            if grid[nr][nc] == 1 and not visited[nr][nc] :
                visited[nr][nc] = True
                size += 1
                q.append((nr, nc))
    return size 

cnt = 0
max_size = 0

for i in range(n) :
    for j in range(m) :
        if grid[i][j] == 1 and not visited[i][j] :
            cnt += 1
            current_size = bfs(i,j)
            max_size = max(max_size, current_size)
print(cnt)
print(max_size)