re_li = []

for _ in range(10) :
    num = int(input())
    re_li.append(num % 42)

re_li = set(re_li)

print(len(re_li))