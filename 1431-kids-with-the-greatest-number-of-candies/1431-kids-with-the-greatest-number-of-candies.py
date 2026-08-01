class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = candies[0]
        ans = [False] * len(candies)
        for num in candies:
            if num > maximum:
                maximum = num
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                ans[i] = True
            else:
                ans[i] = False
        return ans