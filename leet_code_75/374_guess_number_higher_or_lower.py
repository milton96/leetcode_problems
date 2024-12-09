def guess(n):
    pick = 1702766719
    if n > pick:
        return -1
    
    if n < pick:
        return 1
    
    return 0

def guessNumber(n: int) -> int:
    low = 0
    high = n
    while low <= high:
        t = (low + high) // 2
        r = guess(t)

        if r == 0:
            return t
        
        if r == -1:
            high = t - 1
        else:
            low = t + 1

if __name__ == "__main__":
    n = guessNumber(2126753390)
    print(n)