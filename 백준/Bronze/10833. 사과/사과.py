N = int(input())
r_num = 0 # 남는 개수의 합

for _ in range(N) :
    s_num, a_num = map(int,input().split()) # 사과의 수 , 학생의 수
    if (a_num >= s_num) :      # '사과의 수 >= 학생의 수' 라면
        r_num += a_num % s_num 
    else :                     # '사과의 수 <= 학생의 수' 라면
        r_num += a_num         # 나눠주지 않음

print(r_num)