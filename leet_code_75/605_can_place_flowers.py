def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and ((i == len(flowerbed) - 1) or flowerbed[i + 1] == 0) and (i == 0 or flowerbed[i - 1] == 0):
            n-=1
            flowerbed[i] = 1
            if n == 0:
                return True
    
    return n == 0


if __name__ == "__main__":
    flowerbed = [0,0,1,0,1]
    n = 1
    o = canPlaceFlowers(flowerbed, n)
    print(o)