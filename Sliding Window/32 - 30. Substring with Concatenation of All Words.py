class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        word_len = len(words[0])
        total_len = len(words) * word_len
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        result = []
        for i in range(len(s) - total_len + 1):
            seen = {}
            for j in range(i, i + total_len, word_len):
                word = s[j:j+word_len]
                if word not in count:
                    break
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > count[word]:
                    break
            else:
                result.append(i)
        return result