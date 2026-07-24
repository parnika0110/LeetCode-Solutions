class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        rev = ""
        for char in s:
            if 65 <= ord(char) <= 90:
                char = chr(ord(char) + 32)
            if char.isalnum():
                ans += char
        for char in ans:
            rev = char + rev
        return rev == ans
