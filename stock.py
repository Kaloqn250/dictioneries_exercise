stock_info = input().split()
searching_stock = input().split()

stock = {}

for i in range(0, len(stock_info), + 2):
    product = stock_info[i]
    quantity = stock_info[i + 1]
    quantity = int(quantity)

    stock[product] = quantity

for check_stock in searching_stock:
    if check_stock in stock:
        print(f'We have {stock[check_stock]} of {check_stock} left')
    else:
        print(f'Sorry, we don\'t have {check_stock}')
