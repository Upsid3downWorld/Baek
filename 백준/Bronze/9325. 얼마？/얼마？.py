for _ in range(int(input())) :
    total_price = 0
    price_car = int(input())
    total_price += price_car
    for _ in range(int(input())) :
        amount, each_price = map(int, input().split())
        total_price += amount * each_price
    print(total_price)
