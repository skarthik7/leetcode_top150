class Solution:
   def groupAnagrams(self, strs):
        result = collections.defaultdict(list)
        #print(ans)
        
        for s in strs:
            count_letters = [0] * 26
            for c in s:
                count_letters[ord(c) - ord("a")] += 1
            result[tuple(count_letters)].append(s)
        return result.values()