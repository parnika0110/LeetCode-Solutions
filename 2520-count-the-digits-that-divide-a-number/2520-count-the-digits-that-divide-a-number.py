class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        original = num
        while num > 0:
            val = num % 10
            if val != 0:
                if original % val == 0:
                    count += 1
            num //= 10
        return count