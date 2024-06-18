class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        left_idx = binary_search(target)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, binary_search(target + 1) - 1]