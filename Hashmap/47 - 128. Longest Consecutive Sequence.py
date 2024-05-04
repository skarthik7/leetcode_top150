class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        setnums = set(nums)

        for n in setnums:
            if (n-1) not in setnums:
                length = 1
                while (n+length) in setnums:
                    length += 1
                longest = max(longest, length)
        
        return longest