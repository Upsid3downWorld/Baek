sen = []

A, B = map(int,input().split())
for i in range(B+1) :
   for j in range(i) :
       if len(sen) == B :
           break
       sen.append(i)
print(sum(sen[A-1:B]))