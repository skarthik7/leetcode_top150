class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        while len(nums) > 0:
            diff = target - nums.pop()

            if diff in nums:
                pos = nums.index(diff)
                return [pos, len(nums)]