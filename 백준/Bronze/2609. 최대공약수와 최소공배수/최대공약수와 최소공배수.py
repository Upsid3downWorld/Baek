N1, N2 = map(int, input().split())

def get_gcd(N1, N2) :
    while N2 > 0 :
        N1, N2 = N2, N1 % N2
    return N1

def get_lcm(N1, N2) :
    return (N1*N2) // (get_gcd(N1, N2))

print(get_gcd(N1, N2))
print(get_lcm(N1, N2))