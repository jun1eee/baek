# m, n = map(int,input().split())
# num = int(input())
# if num > n * m:
#     print(0)
#     exit()
# visited = [[False]*m for _ in range(n)]
# dirs = [(1,0),(0,1),(-1,0),(0,-1)]
# r, c = 0, 0
# dir_idx = 0
# for i in range(1,num):
#     visited[r][c] = True
#     nr, nc = r + dirs[dir_idx][0], c + dirs[dir_idx][1]
#     if nr < 0 or nr >= n or nc < 0 or nc >= m or visited[nr][nc]:
#         dir_idx = (dir_idx + 1) % 4
#         nr, nc = r + dirs[dir_idx][0], c + dirs[dir_idx][1]
#     r, c = nr, nc
# print(c+1, r+1)
from collections import deque
m, n = map(int,input().split())
num = int(input())
if num > n * m:
    print(0)
    exit()
seats = [[0]*m for _ in range(n)]
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
q = deque()
q.append((0,0,1))
seats[0][0] = 1
dirs_index = 0
while q:
    r, c, cnt = q.popleft()
    if cnt == num:
        print(c+1, r+1)
        break
    nr, nc = r + dirs[dirs_index][0], c + dirs[dirs_index][1]
    if nr < 0 or nr >= n or nc < 0 or nc >= m or seats[nr][nc]!=0:
        dirs_index = (dirs_index + 1) % 4
        nr, nc = r + dirs[dirs_index][0], c + dirs[dirs_index][1]

    seats[nr][nc] = cnt + 1
    q.append((nr,nc,cnt + 1))