def removeStars(s: str) -> str:
    star_count = s.count("*")
    l = len(s)
    if (l/2) == star_count:
        return ""
    
    stack = []
    for i in range(l):
        if s[i] != "*":
            stack.append(s[i])
        elif s[i] == "*":
            stack.pop()
    return "".join(stack)

if __name__ == "__main__":
    s = "leet**cod*e"
    print(removeStars(s))