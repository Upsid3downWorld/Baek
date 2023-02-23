import math

A, I = map(int,input().split())

ans = A * I

while (math.ceil(ans / A) >= I) :
    ans -= 1
    

print(ans+1)
