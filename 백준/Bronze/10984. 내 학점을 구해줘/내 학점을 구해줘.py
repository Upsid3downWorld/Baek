T = int(input())

for _ in range(T) :
    total_c = 0
    total_g = 0
    N = int(input())
    for _ in range(N) :
        c, g = map(float, input().split())
        total_c += c
        total_g += c * g

    gpa = total_g / total_c
    
    print(int(total_c), '%.1f' % gpa)