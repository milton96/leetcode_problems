def reverseVowels(s: str) -> str:
    #v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    v = "aeiouAEIOU"
    c = []
    reverse = ""
    for i in range(len(s)):
        if s[i] in v:
            c.append(i)
    for i in range(len(s)):
        if s[i] in v:
            reverse += s[c.pop()]
        else:
            reverse += s[i]
            
    return reverse

if __name__ == "__main__":
    s = "hello"
    o = reverseVowels(s)
    print(o)