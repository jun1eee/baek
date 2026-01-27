left = list(input())
right = []
n = int(input())

for _ in range(n):
    command = input()
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[2])
answer = left + right[::-1]
print(''.join(answer))