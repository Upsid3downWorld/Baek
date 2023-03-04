n = int(input()) # 테스트 케이스의 개수
for _ in range(n) :
    p = int(input()) # 고려해야될 선수의 수
    high_price = 0
    high_price_player = ""
    for _ in range(p) :    
        price, player = map(str, input().split())
        price = int(price)

        if ( price > high_price ) :
            high_price = price
            high_price_player = player
    print(high_price_player)
    
