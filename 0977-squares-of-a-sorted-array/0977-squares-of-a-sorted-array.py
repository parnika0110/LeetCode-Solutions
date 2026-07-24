class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i] * nums[i]
        ans.sort()
        return ans