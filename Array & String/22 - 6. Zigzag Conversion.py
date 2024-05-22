class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        L = [''] * numRows
       
        index, step = 0, 1

        for ele in s:
            L[index] += ele
           
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            
            index += step

        return ''.join(L)