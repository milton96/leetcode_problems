from math import gcd

def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    return str1[:gcd(len(str1), len(str2))]

    

if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    #str1 = "ABCDEF"
    #str2 = "ABC"
    r = gcdOfStrings(str1, str2)
    print(r)