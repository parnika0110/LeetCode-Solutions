class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Step 1: Sort the array to find the median
        nums.sort()
        
        # Step 2: Choose the median as the target value
        median = nums[len(nums) // 2]
        
        # Step 3: Calculate the total moves needed to reach the median
        return sum(abs(num - median) for num in nums)
