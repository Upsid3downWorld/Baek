s_h, s_m, s_s = map(int, input().split(":"))
e_h, e_m, e_s = map(int, input().split(":"))


r_t = (e_h*3600) - (s_h*3600) + (e_m*60) - (s_m*60) + (e_s) - (s_s)

if (r_t) < 0 :
    r_t += 60*60*24

h = r_t // 3600
m = (r_t % 3600) // 60
s = (r_t % 3600) % 60

print("%02d:%02d:%02d" % (h, m, s))
