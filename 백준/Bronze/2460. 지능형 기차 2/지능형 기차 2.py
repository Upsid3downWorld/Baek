p_list = []
t_p = 0

for _ in range(10) :
    land_p, board_p = map(int, input().split())
    t_p = t_p - land_p + board_p
    p_list.append(t_p)

print(max(p_list))