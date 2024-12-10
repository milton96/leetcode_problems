def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n&1 # Compare bits of n and 1
        n = n>>1 # Divide between 2
    return count

if __name__ == "__main__":
    test = [11, 128, 2147483645, 2, 9]

    for i in test:
        ans = hammingWeight(i)
        print(ans)
