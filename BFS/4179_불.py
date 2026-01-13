from collections import deque
R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
dist = [[-1] * C for _ in range(R)]
