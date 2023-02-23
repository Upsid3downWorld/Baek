T = int(input())

for _ in range(T) :
    R, S = input().split()
    sen = ""
    for i in S :
        sen += int(R) * i
    print(sen)