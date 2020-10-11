def stock(stocks):
    if not stocks or len(stocks) == 0:
        return 0
    
    res = 0
    min_s = float('inf')
    for s in stocks:
        min_s = min(min_s, s)
        res = max(res, s-min_s)
    return res

stocks = [9,8,7,6,5]
print(stock(stocks))