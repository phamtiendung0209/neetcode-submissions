from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Write your solution here.
        output = []

        has_zero = False 
        multiple_zeros = False 
        zero_counter = 0

        for num in nums:
            if num == 0:
                zero_counter += 1
                has_zero = True

        if zero_counter >= 2:
            multiple_zeros = True

        product = 1
        for num in nums:
            if num != 0:
                product *= num

        for num in nums:
            if has_zero == False:
                output.append(product // num)
            elif has_zero == True and multiple_zeros == False: 
                if num == 0:
                    output.append(product)
                else:
                    output.append(0)
            elif multiple_zeros == True: 
                output.append(0)

        return output


solution = Solution()