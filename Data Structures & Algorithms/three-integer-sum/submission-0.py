from typing import List

class Solution:

    def twoSum(self, nums, start, target):
        pairs = []
        left = start
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum < target:
                left += 1

            elif current_sum > target:
                right -= 1

            else:
                pairs.append([nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicate pairs
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums) - 2):

            # Skip duplicate fixed elements
            # i > 0 makes sure we don't check nums[0] == nums[-1]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 1: Fix one element
            fixed = nums[i]

            # Step 2: Find two elements summing to -fixed
            target = -fixed
            pairs = self.twoSum(nums, i + 1, target)

            # Step 3: Combine the fixed element with each pair
            for pair in pairs:
                output.append([fixed] + pair)

        return output