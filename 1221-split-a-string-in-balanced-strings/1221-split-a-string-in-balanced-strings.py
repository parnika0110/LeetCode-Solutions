class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        bal = 0
        for char in s:
            if char == "L":
                bal += 1
            elif char == "R":
                bal -= 1
            if bal == 0:
                count += 1
        return count