from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Write your solution here.
        groups = {}

        for word in strs:
            # Key insight: Two strings are anagrams if their sorted characters are identical
            
            # Convert each word into a string because lists cannot be dictionary keys, but strings can
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
        
solution = Solution()