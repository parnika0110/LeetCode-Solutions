class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)
        for i in range(1,len(nums)):
            leftSum[i] = leftSum[i-1] + nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            rightSum[j] = rightSum[j+1] + nums[j+1]
        for i in range(len(nums)):
            answer[i] = abs(leftSum[i] - rightSum[i])
        return answer
         