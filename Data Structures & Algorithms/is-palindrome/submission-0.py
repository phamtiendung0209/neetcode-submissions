class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Write your solution here.
        reduced_s = [char for char in s if char.isalnum()]

        left = 0
        right = len(reduced_s) - 1

        while left < right:
            if reduced_s[left].lower() != reduced_s[right].lower():
                return False 

            left += 1
            right -= 1

        return True


solution = Solution()