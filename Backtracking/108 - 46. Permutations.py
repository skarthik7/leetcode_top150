class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack([], nums, result)
        return result

    def backtrack(self, curr, nums, result):
        if len(curr) == len(nums):
            result.append(curr[:])
            return
        for num in nums:
            if num not in curr:
                curr.append(num)
                self.backtrack(curr, nums, result)
                curr.pop()