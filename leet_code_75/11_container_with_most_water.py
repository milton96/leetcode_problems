def maxArea(height: list[int]) -> int:
    l = 0
    r = len(height) - 1
    ans = 0
    while l < r:
        w = r - l
        h = min(height[l], height[r])
        area = w * h
        ans = max(ans, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return ans

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    ans = maxArea(height)
    print(ans)