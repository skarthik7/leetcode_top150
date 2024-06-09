class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            common_bits = ones & twos
            ones &= ~common_bits
            twos &= ~common_bits
        return ones