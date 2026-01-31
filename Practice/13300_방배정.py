import sys
input = sys.stdin.readline

n, k = map(int, input().split())
students = [[0] * 7 for _ in range(2)]

for _ in range(n):
    s, y = map(int, input().split())
    students[s][y] += 1

ans = 0
for y in range(1, 7):
    ans += (students[0][y] + k - 1) // k
    ans += (students[1][y] + k - 1) // k

print(ans)