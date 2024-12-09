def uniqueOccurrences(arr: list[int]) -> bool:
    counts = {}
    repeat = []
    for n in arr:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1

    for c in counts:
        if counts[c] in repeat:
            return False
        else:
            repeat.append(counts[c])

    return True
if __name__ == "__main__":
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    print(uniqueOccurrences(arr))