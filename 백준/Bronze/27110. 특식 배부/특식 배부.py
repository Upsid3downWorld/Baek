N = int(input())
A, B, C = map(int,input().split())
m_p = 0

if ( A > N ) :
    m_p += N
else :
    m_p += A
    
if ( B > N ) :
    m_p += N
else :
    m_p += B
    
if ( C > N ) :
    m_p += N
else :
    m_p += C

print(m_p)
