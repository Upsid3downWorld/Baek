m5_count = 0
m1_count = 0
s10_count = 0

T = int(input())

if (T % 10 != 0) :
    print(-1)
else :
    while ( T >= 300 ) :
        m5_count += 1
        T -= 300

    while (( 300 > T ) and ( T >= 60 )) :
        m1_count += 1
        T -= 60

    while (( 60 > T ) and ( T > 0 )) :
        s10_count += 1
        T -=10

    print(m5_count, m1_count, s10_count)


    
