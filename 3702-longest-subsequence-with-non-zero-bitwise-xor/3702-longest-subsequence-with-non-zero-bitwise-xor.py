class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        zeros = 0

        for num in nums:
            xor ^= num
            if num == 0:
                zeros += 1

        if xor != 0:
            return len(nums)

        if zeros == len(nums):
            return 0

        return len(nums) - 1