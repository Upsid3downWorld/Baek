T = int(input()) # 테스트 케이스의 숫자 T

for _ in range(T) :
    N = int(input()) # 학교의 숫자 정수 N
    m_drink = 0      # 가장 많이 소비한 양
    m_school = ""    # 가장 많은 양을 소비한 학교명
    for _ in range(N) :
        s_name, s_drink = input().split() # 학교명과 학교별 소비한 양
        s_drink = int(s_drink)            # 비교를 위해 정수형으로 형변환
        if (s_drink > m_drink) :          # 기존에 가장 많이 소비한 양보다 더 많은 양을 소비한다면
            m_drink = s_drink             
            m_school = s_name
    print(m_school)
    
    
