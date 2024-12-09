def majorityElement(nums: list[int]) -> int:
    l = len(nums) // 2
    counts = {}
    for n in nums:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1

    for k, v in counts.items():
        if v > l:
            return k
    return 0

if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(majorityElement(nums))