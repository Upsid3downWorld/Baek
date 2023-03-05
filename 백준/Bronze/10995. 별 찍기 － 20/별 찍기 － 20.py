N = int(input())

if (N == 1) :
    print("*")
if (N > 1) :
    for i in range(1,N+1) :
        
        if ( i % 2 != 0 ) : # 홀수라면
            print("*" + " *" * (N-1))
        else : # 짝수라면
            print(" *" * N)
 
        
        
    
