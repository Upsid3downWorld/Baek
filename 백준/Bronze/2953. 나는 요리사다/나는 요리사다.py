score_list = []

for _ in range(5) :
    a = list(map(int, input().split()))
    score_list.append(sum(a))

print((score_list.index(max(score_list))+1), max(score_list))