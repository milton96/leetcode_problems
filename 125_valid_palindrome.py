def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = "".join([char for char in s if char.isalnum()])
    
    return s == s[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    sol = isPalindrome(s)
    print(sol)