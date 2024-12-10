def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    n = n + 1
    ans = [0] * n

    ans[0] = 0
    ans[1] = 1
    ans[2] = 1

    for i in range(3, n):
        ans[i] = ans[i-1] + ans[i-2] + ans[i-3]

    return ans[n-1]

if __name__ == "__main__":
    data = 25
    sol = tribonacci(data)
    print(sol)