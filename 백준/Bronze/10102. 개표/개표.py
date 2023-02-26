V = int(input()) 
W = list(input())

cnt_A = 0
cnt_B = 0

for i in W :
    if (i == 'A') :
        cnt_A += 1
    elif (i == 'B') :
        cnt_B += 1

if (cnt_A > cnt_B) :
    print ("A")
elif (cnt_B > cnt_A) :
    print ("B")
else :
    print("Tie")
