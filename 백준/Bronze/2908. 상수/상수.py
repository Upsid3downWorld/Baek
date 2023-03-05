num_list = []
a, b = input().split()
num_list.append(a[::-1])
num_list.append(b[::-1])

if (num_list[0] > num_list[1]) :
    print(num_list[0])
else :
    print(num_list[1])