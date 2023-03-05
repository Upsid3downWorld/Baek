N = int(input())
score_list = list(map(int, input().split()))
total_score = 0
combo = 0
combo_li = []

for i in range(N) :
    if (i == 0) :
        if (score_list[i] == 1) :
            combo += 1
            combo_li.append(combo)
    else : 
        if (score_list[i] == 0) : 
            combo = 0
        elif (score_list[i] == 1) : 
            combo += 1
            combo_li.append(combo)
            
print(sum(combo_li))