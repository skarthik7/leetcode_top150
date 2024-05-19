class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = current_jump_end = furthest = 0
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = furthest
        return jumps