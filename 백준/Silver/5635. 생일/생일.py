import sys
input = sys.stdin.readline

b_list = []
n = int(input())
for _ in range(n) :
    n, d, m, y = input().split()
    d, m, y = map(int,(d,m,y))
    b_list.append((y,m,d,n))

b_list.sort()

print(b_list[-1][3])
print(b_list[0][3])
