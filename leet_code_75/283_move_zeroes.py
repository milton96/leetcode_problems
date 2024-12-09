def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    if l == 1:
        return
    nums.sort()
    li  = l - nums[::-1].index(0)
    a = nums[li:]
    a.extend(nums[:li])
    nums = a.copy()[::-1]

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    print(nums)