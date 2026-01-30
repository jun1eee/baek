word = input()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for a in alpha:
    check = False
    for i, w in enumerate(word):
        if w == a:
            check = True
            print(i, end=" ")
            break
    if check:
        continue
    print(-1, end=" ")

# word = input()

# for c in range(ord('a'), ord('z')+1):
#     print(word.find(chr(c)), end=' ')
