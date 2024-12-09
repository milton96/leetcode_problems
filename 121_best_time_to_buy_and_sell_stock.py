
def maxProfit(prices: list[int]) -> int:
    min_value = float('inf')
    max_value = 0

    for p in prices:
        if p < min_value:
            min_value = p
        profit = p - min_value
        if profit > max_value:
            max_value = profit

    return max_value


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
