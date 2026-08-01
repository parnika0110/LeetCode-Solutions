class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            current = nums[i]
            needed = target - current
            if needed in seen:
                return i, seen[needed]
            else:
                seen[current] = i 



