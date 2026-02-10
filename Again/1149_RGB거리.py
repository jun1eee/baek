import sys
input = sys.stdin.readline
n = int(input())
r,g,b = map(int,input().split())
for _ in range(n-1):
    nr, ng, nb = map(int,input().split())
    r, g, b = nr + min(g,b), ng + min(r,b), nb + min(r,g)
print(min(r,g,b))