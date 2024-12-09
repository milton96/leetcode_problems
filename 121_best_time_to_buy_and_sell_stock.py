
def maxProfit(prices: list[int]) -> int:
    m = min(prices)
    if m == prices[-1]:
        return 0
    i = prices.index(m)
    m_v = max(prices[i+1:])
    return m_v - m



if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    m = maxProfit(prices)
    print("hola")