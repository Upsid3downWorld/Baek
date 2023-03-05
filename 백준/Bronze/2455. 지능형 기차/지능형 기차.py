people_li = []
total_p = 0

for _ in range(4) :
    land_p ,board_p = map(int, input().split())
    total_p = total_p - land_p + board_p
    people_li.append(total_p)

print(max(people_li))