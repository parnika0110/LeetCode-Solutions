class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        rev = 0
        if x < 0:
            negative = True
            x = -x
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        if negative:
            rev = -rev
        if rev < -(2**31) or rev > (2**31)-1:
            return 0
        else:
            return rev