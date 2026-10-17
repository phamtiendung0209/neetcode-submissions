class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]: # The left half is ascending
                if nums[lo] <= target < nums[mid]: # The target is between [lo, mid - 1]
                    hi = mid - 1
                else: # The target is between [mid + 1, hi]
                    lo = mid + 1 
            else: # The right half is ascending
                if nums[mid] < target <= nums[hi]: # The target is between [mid + 1, hi]
                    lo = mid + 1
                else: # The target is between [lo, mid - 1]
                    hi = mid - 1

        return -1
        