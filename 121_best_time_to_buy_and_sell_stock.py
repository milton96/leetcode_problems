
def maxProfit(prices: list[int]) -> int:
    min_value = prices[0]
    for i in range(1, len(prices)):
        if prices[i] <= min_value:
            min_value = prices[i]
        else:
            m = min(prices[i+1:])
            if m <= min_value:
                min_value = m
            break
    index = prices.index(min_value)
    prices_sliced = prices[index+1:]
    if len(prices_sliced) == 0:
        return 0
    max_value = max(prices[index+1:])
    return max_value - min_value


if __name__ == "__main__":
    prices = [
        [7,1,5,3,6,4],
        [7,6,4,3,1],
        [2,4,1],
        [2,1,2,0,1],
        [2,1,2,1,0,1,2]
    ]
    for price in prices:
        sol = maxProfit(price)
        print(sol)
