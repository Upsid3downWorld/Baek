for _ in range(int(input())) :
    l, s = list(input().split())
    for i in range(len(s)) :
        if (i == (int(l)-1)) :
            continue
        else :
            print(s[i], end = "")
    print()