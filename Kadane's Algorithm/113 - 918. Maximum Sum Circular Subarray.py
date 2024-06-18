class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            current_sum = max_sum = nums[0]
            for num in nums[1:]:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum
        max_sum = kadane(nums)
        circular_sum = sum(nums) + kadane([-num for num in nums])
        return max(max_sum, circular_sum) if circular_sum else max_sum