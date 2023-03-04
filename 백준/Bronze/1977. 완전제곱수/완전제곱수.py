import math
M = int(input())
N = int(input())
s_num = []
for i in range(1, math.isqrt(N)+1) :
    if (math.pow(i,2) >= M) and (math.pow(i,2) <= N) :
        s_num.append(int(math.pow(i,2)))

if len(s_num) > 0 :
    print(sum(s_num))
    print(s_num[0])
else :
    print(-1)