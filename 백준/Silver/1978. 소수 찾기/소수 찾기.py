n = int(input())
numbers = map(int, input().split())
n_sosu = 0

for num in numbers :
    if (num == 1) :
        n_sosu += 1
    for i in range(2, num) :
        if (num % i == 0) :
            n_sosu += 1
            break

print(n - n_sosu)