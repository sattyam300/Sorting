def buyChocolates(prices, money):
    prices.sort()
    return prices[0] + prices[1] <= money
