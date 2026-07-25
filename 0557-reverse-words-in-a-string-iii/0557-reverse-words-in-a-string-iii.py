class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = []
        for word in words:
            left = 0
            right = len(word) - 1
            word = list(word)
            while left < right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            ans.append("".join(word))
        return " ".join(ans)