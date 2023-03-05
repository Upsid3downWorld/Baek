num_list = []
m_count = 0
m_num = 0

for _ in range(10) :
    num_list.append(int(input()))

for i in range(len(num_list)) :
    if num_list.count(num_list[i]) > m_count :
        m_count = num_list.count(num_list[i])
        m_num = num_list[i]

print("%d" % (sum(num_list)/10))
print(m_num)