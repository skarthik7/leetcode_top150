class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        while start < len( nums):
            if nums.count(nums[start]) > 1:
                nums.remove(nums[start])
                start -= 1
            start += 1