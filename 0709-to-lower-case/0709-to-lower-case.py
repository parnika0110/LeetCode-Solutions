class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for char in s:
            if 65 <= ord(char) <= 90:
                char = chr(ord(char) + 32)
                ans += char
            else:
                ans += char
        return ans