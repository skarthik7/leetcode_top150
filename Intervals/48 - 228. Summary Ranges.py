class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = [] 
        for num in nums:
            if ranges and ranges[-1][1] == num-1:
                ranges[-1][1] = num
            else:
                ranges.append([num, num])

        return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]