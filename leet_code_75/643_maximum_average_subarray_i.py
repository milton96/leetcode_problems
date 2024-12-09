def findMaxAverage(nums: list[int], k: int) -> float:
    val = float("-inf")
    for i in range(len(nums)-k+1):
        s = sum(nums[i:k+i])
        val = max(val, s)

    return val/k

if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    r = findMaxAverage(nums, k)
    print(r)