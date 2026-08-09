class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for char in magazine:
            if char not in count:
                count[char] = 0
            count[char] += 1

        for char in ransomNote:
            if char not in count or count[char] == 0:
                return False

            count[char] -= 1

        return True