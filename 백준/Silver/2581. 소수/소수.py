M = int(input())
N = int(input())

sosu_list = []

for i in range(M,N+1) : # i = M~N 범위의 숫자
    n_sosu = 0
    if i > 1:
        for j in range(2,i) : # j = 2 ~i-1 범위의 숫자
            if (i % j == 0) :
                n_sosu += 1
                break
        if (n_sosu ==0) :
            sosu_list.append(i)
    
        
if (len(sosu_list) > 0) :
    print(sum(sosu_list))
    print(min(sosu_list))     
else :
    print(-1)
