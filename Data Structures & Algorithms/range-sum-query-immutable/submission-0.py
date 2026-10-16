from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()

    def sumRange(self, left: int, right: int) -> int:
        prefix = [0]

        for num in self.nums:
            prefix.append(prefix[-1] + num)
        
        return prefix[right + 1] - prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)