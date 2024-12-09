def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    o = []
    m = max(candies)
    for i in candies:
        o.append((i + extraCandies) >= m)        
    return o

if __name__ == "__main__":
    candies = [2,3,5,1,3]
    extraCandies = 3
    o = kidsWithCandies(candies, extraCandies)
    print(o)