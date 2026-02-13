import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u,v,d = map(int,input().split())
    graph[u].append((v,d))
    graph[v].append((u,d))

def bfs(start):
    q = deque([start])
    visited = [-1] * (n+1)
    visited[start] = 0
    while q:
        cur = q.popleft()
        for next, next_dist in graph[cur]:
            if visited[next] == -1:
                visited[next] = visited[cur] + next_dist
                q.append(next)
    m = max(visited)
    return [visited.index(m), m]
print(bfs(bfs(1)[0])[1])    
# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline
# n = int(input())
# graph = [[] for _ in range(n+1)]

# for _ in range(n-1):
#     u, v, d = map(int, input().split())
#     graph[u].append((v,d))
#     graph[v].append((u,d))

# def dfs(start, distance):
#     for next, next_dist in graph[start]:
#         if visited[next] == -1:
#             visited[next] = distance + next_dist
#             dfs(next, distance + next_dist)

# visited = [-1] * (n+1)
# visited[1] = 0
# dfs(1,0)

# last_node = visited.index(max(visited))
# visited = [-1] * (n+1)
# visited[last_node] = 0
# dfs(last_node,0)
# print(max(visited))