area = [[0 for col in range(100)] for row in range(100)]

for _ in range(int(input())) :
    l, b = map(int, input().split())
    for i in range(l, l+10) :
        for j in range(b, b+10) :
            area[i][j] = 1

cnt = 0

for i in range(100) :
    cnt += area[i].count(1)

print(cnt)