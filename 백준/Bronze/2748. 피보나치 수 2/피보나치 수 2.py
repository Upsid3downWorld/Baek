n = int(input())
p0 = 0
p1 = 1

for i in range(n//2) :
    p0 = p0 + p1
    p1 = p0 + p1
    
if ( n % 2 == 0 ) :
    print(p0)
else :
    print(p1)

