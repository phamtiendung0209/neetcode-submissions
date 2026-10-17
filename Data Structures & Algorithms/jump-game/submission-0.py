class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Main idea: Instead of deciding exactly where to jump, we track the furthest index 
        # we can possibly reach
        # Use one fariable farthest: The largest index we know we can reach from index 0, potentially 
        # using multiple jumps
        # At each index, we ask two questions:
        #   1. Can we reach this index?
        #   2. If so, can jumping from here increase farthest?
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) - 1:
                return True

        return False