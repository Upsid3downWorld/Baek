import math

result = 0

for i in map(int, input().split()) :
    result += math.pow(i,2)

print("%.f" % (result % 10))