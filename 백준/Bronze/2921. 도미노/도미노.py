N = int(input())
domino = 0

for i in range(1, N+2) :
    domino += i

print(domino * N)
