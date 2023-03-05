sen = []

A, B = map(int,input().split())
for i in range(1, B+1) :
    for _ in range(i) :
        if len(sen) == B :
            break
        sen.append(i)
print(sum(sen[A-1:B]))
