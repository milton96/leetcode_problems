def getSum(a: int, b: int) -> int:
    mask = 0xffffffff
    while b & mask != 0:
        aux = (a&b)<<1
        a = a ^ b
        b = aux
    return a & mask if  b > 0 else a


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