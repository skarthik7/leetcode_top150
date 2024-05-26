import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        map_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits)==1:
            return [i for i in map_dict[digits[0]]]
        strings=[]
        for ele in digits:
            strings.append(map_dict[ele])
        return [''.join(combination) for combination in itertools.product(*strings)]