class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        return any (v > 1 for v in count.values())