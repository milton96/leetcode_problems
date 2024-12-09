def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

if __name__ == "__main__":
    data = [
        [1,2,3,1],
        [1,2,3,4],
        [1,1,1,3,3,4,3,2,4,2]
    ]
    for d in data:
        sol = containsDuplicate(d)
        print(sol)