from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        boundary = 0
        scan = 0
        last_unknown = len(nums) - 1

        while scan <= last_unknown:
            if nums[scan] == 0:
                nums[boundary], nums[scan] = nums[scan], nums[boundary]
                scan += 1
                boundary += 1

            elif nums[scan] == 2:
                nums[last_unknown], nums[scan] = nums[scan], nums[last_unknown]
                last_unknown -= 1

            else: 
                scan += 1