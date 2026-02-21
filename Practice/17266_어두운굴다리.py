import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = list(map(int,input().split()))
heights = [arr[0],n-arr[-1]]
for i in range(1,m):
    heights.append((arr[i]-arr[i-1]+1)//2)
print(max(heights))