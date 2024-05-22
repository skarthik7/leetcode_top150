class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines, line, length = [], [], 0
        for word in words:
            if length + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - length):
                    line[i%(len(line)-1 or 1)] += ' '
                lines.append(''.join(line))
                line, length = [], 0
            line.append(word)
            length += len(word)
        return lines + [' '.join(line).ljust(maxWidth)]