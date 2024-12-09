def getSum(a: int, b: int) -> int:
    while b != 0:
        aux = a&b
        a = a ^ b
        b = aux<<1 
    return a


if __name__ == "__main__":
    data = [
        [1,2],
        [2,3],
        [100,99],
        [-1,1]
    ]
    for d in data:
        sol = getSum(d[0], d[1])
        print(sol)