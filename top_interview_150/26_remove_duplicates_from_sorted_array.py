def removeDuplicates(nums: list[int]) -> int:
    n = list(set(nums))
    l_n = len(n)
    l_nums = len(nums)
    for i in range(l_nums - l_n, l_nums - 1):
        n.append(0)
    
    return l_n

if __name__ == "__main__":
    n1 = [1,1,2]
    ex = [1,2,0]
    k = removeDuplicates(n1)
    for i in range(k):
        print(n1[i], ex[i])
