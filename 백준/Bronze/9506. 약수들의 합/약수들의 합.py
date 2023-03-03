while True :
    n = int(input())
    if ( n == -1 ) : # n의 값이 -1일 경우 
        break        # 반복문 종료
    div = []         # 약수가 들어갈 리스트
    for i in range(1, n) :
        if (n % i == 0) : # 나머지가 0(약수)이라면
            div.append(i) # 약수가 들어갈 리스트에 요소로 추가
    if sum(div) == n : # 약수들의 합이 n의 값과 같다면(완전수라면)
        #print(n, " = ", " + ".join(str(i) for i in div), sep="")
        print(n, "=", end=" ")
        print(*div, sep=" + ")
    else :
        print(n, "is NOT perfect.")
