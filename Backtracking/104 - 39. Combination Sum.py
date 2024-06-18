class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(0, [], target, candidates, result)
        return result

    def backtrack(self, start, curr, target, candidates, result):
        if target == 0:
            result.append(curr[:])
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            curr.append(candidates[i])
            self.backtrack(i, curr, target - candidates[i], candidates, result)
            curr.pop()