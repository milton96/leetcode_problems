def twoSum(nums: list[int], target: int) -> list[int]:
    l = len(nums)
    if l == 2:
        return [0,1]
    map = {}
    for i in range(l):
        t = target - nums[i]
        if t in map:
            return [i, map[t]]
        map[nums[i]] = i
        
    return []

if __name__ == "__main__":
    nums = [3,2,3]
    target = 6
    o = twoSum(nums, target)
    print(o)