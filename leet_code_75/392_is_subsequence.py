def isSubsequence(s: str, t: str) -> bool:
    ls, lt = len(s), len(t)

    if ls == 0 and lt == 0:
        return True
    if lt == 0:
        return False

    i_s, i_t = 0, 0

    while i_s < ls:
        if s[i_s] == t[i_t]:
            i_s += 1
            i_t += 1
        else:
            i_t += 1

        if i_s < ls and i_t == lt:
            return False
        
    return True

if __name__ == "__main__":
    s = "axc"
    t = "ahbgdc"
    sol = isSubsequence(s, t)
    print(sol)