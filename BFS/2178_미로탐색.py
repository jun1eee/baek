from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs() :
    q = deque()
    q.append((0,0))
    dist[0][0] = 1
    cnt = 1
    
    while q :
        r,c = q.popleft()
        if r == n-1 and c == m -1 :
            return dist[n-1][m-1]
        for dr, dc in dirs :
            nr, nc = r + dr, c + dc
            if 0 > nr or n <= nr or 0 > nc or m <= nc :
                continue
            if grid[nr][nc] == 1 and dist[nr][nc] == 0 :
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr,nc))

print(bfs())