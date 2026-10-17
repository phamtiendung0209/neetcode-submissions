class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ending = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            ending = max(nums[i], ending + nums[i])
            best = max(best, ending)

        return best
        