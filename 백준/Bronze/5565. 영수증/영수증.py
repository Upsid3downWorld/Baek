price_list = []
total_price = int(input())

for _ in range(9) :
    price = int(input())
    price_list.append(price)

print(total_price-sum(price_list))
    
