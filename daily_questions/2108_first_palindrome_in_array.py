def firstPalindrome(words: list[str]) -> str:
    for word in words:
        if word == word[::-1]:
            return word
    return ""

if __name__ == "__main__":
    words = ["abc","car","ada","racecar","cool"]
    palindromo = firstPalindrome(words)
    print(palindromo)