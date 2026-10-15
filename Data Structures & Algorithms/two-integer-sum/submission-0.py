class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Write your solution here.
        others = [target - num for num in nums]

        # Use dictionary for fast in search
        # Remember that searching for dictionaries is O(1) in keys (converted to hash values) but still O(n) in values
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i 

        for i, other in enumerate(others):
            if other in nums_dict.keys() and i != nums_dict[other]:
                return sorted([i, nums_dict[other]])